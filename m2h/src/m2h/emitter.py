# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2026 Takayuki Nagata

"""Hack assembly emitter for MSP430 statements."""

from m2h.parser import Operand, OperandType, Statement


def sanitize_symbol(name: str) -> str:
    """Sanitize symbols and labels for Hack Assembler compatibility."""
    if not name:
        return ""
    # Replace leading dot with DOT_ if needed, keep valid chars
    if name.startswith("."):
        return f"DOT_{name[1:]}"
    return name


def reg_to_hack_symbol(reg_name: str) -> str:
    """Map normalized MSP430 register name (r0..r15) to Hack predefined symbol."""
    reg = reg_name.lower()
    if reg in ("r0", "pc"):
        return "R0"
    if reg in ("r1", "sp"):
        return "SP"
    if reg in ("r2", "sr"):
        return "R2"
    if reg in ("r3", "cg"):
        return "R3"
    # r4..r15 -> R4..R15
    num = reg[1:]
    return f"R{num}"


class HackEmitter:
    """Emits Hack assembly instructions from MSP430 statements."""

    def __init__(self, include_crt0: bool = True) -> None:
        self.include_crt0 = include_crt0
        self.call_counter = 0

    def next_return_label(self) -> str:
        """Generate a unique return label for call instructions."""
        self.call_counter += 1
        return f"__RET_LBL_{self.call_counter}"

    def emit_load_operand(self, op: Operand) -> list[str]:
        """Load the value of an operand into the Hack D register."""
        if op.op_type == OperandType.REGISTER:
            sym = reg_to_hack_symbol(op.value)
            return [f"@{sym}", "D=M"]

        if op.op_type == OperandType.IMMEDIATE:
            val = sanitize_symbol(op.value)
            return [f"@{val}", "D=A"]

        if op.op_type == OperandType.INDIRECT:
            sym = reg_to_hack_symbol(op.value)
            return [f"@{sym}", "A=M", "D=M"]

        if op.op_type == OperandType.INDIRECT_AUTOINC:
            sym = reg_to_hack_symbol(op.value)
            return [f"@{sym}", "A=M", "D=M", f"@{sym}", "M=M+1"]

        if op.op_type == OperandType.INDEXED:
            assert op.reg is not None
            sym = reg_to_hack_symbol(op.reg)
            if op.value == "0":
                return [f"@{sym}", "A=M", "D=M"]
            offset_sym = sanitize_symbol(op.value)
            return [f"@{offset_sym}", "D=A", f"@{sym}", "A=D+M", "D=M"]

        if op.op_type == OperandType.ABSOLUTE:
            sym = sanitize_symbol(op.value)
            return [f"@{sym}", "D=M"]

        raise ValueError(f"Unsupported operand type: {op.op_type}")

    def emit_store_operand(self, op: Operand) -> list[str]:
        """Store the value from the Hack D register into the destination operand."""
        if op.op_type == OperandType.REGISTER:
            sym = reg_to_hack_symbol(op.value)
            return [f"@{sym}", "M=D"]

        if op.op_type == OperandType.INDIRECT:
            sym = reg_to_hack_symbol(op.value)
            return [f"@{sym}", "A=M", "M=D"]

        if op.op_type == OperandType.INDEXED:
            assert op.reg is not None
            sym = reg_to_hack_symbol(op.reg)
            if op.value == "0":
                return [f"@{sym}", "A=M", "M=D"]
            offset_sym = sanitize_symbol(op.value)
            return [
                "@__M2H_TMP_VAL",
                "M=D",
                f"@{offset_sym}",
                "D=A",
                f"@{sym}",
                "D=D+M",
                "@__M2H_TMP_ADDR",
                "M=D",
                "@__M2H_TMP_VAL",
                "D=M",
                "@__M2H_TMP_ADDR",
                "A=M",
                "M=D",
            ]

        if op.op_type == OperandType.ABSOLUTE:
            sym = sanitize_symbol(op.value)
            return [f"@{sym}", "M=D"]

        raise ValueError(f"Cannot store into operand type: {op.op_type}")

    def emit_statement(self, stmt: Statement) -> list[str]:
        """Translate a single Statement into Hack assembly instructions."""
        out: list[str] = []

        if stmt.label:
            lbl = sanitize_symbol(stmt.label)
            out.append(f"({lbl})")

        if stmt.directive:
            # Handle .word / .short data directives
            if stmt.directive in (".word", ".short") and stmt.directive_args:
                for val in stmt.directive_args:
                    clean_val = sanitize_symbol(val)
                    out.extend([f"// .word {val}", f"@{clean_val}", "D=A"])
            return out

        if not stmt.mnemonic:
            return out

        mn = stmt.mnemonic
        ops = stmt.operands

        # 1. mov src, dst
        if mn == "mov":
            if len(ops) != 2:
                raise ValueError(f"mov requires 2 operands, got {len(ops)}")
            src, dst = ops[0], ops[1]
            out.extend(self.emit_load_operand(src))
            out.extend(self.emit_store_operand(dst))
            return out

        # 2. add src, dst
        if mn == "add":
            if len(ops) != 2:
                raise ValueError(f"add requires 2 operands, got {len(ops)}")
            src, dst = ops[0], ops[1]
            if (
                src.op_type == OperandType.IMMEDIATE
                and src.value == "1"
                and dst.op_type == OperandType.REGISTER
            ):
                sym = reg_to_hack_symbol(dst.value)
                return [f"@{sym}", "M=M+1"]
            out.extend(self.emit_load_operand(src))
            if dst.op_type == OperandType.REGISTER:
                sym = reg_to_hack_symbol(dst.value)
                out.extend([f"@{sym}", "M=D+M"])
            else:
                out.extend(["@__M2H_TMP_VAL", "M=D"])
                out.extend(self.emit_load_operand(dst))
                out.extend(["@__M2H_TMP_VAL", "D=D+M"])
                out.extend(self.emit_store_operand(dst))
            return out

        # 3. sub src, dst (dst = dst - src)
        if mn == "sub":
            if len(ops) != 2:
                raise ValueError(f"sub requires 2 operands, got {len(ops)}")
            src, dst = ops[0], ops[1]
            if (
                src.op_type == OperandType.IMMEDIATE
                and src.value == "1"
                and dst.op_type == OperandType.REGISTER
            ):
                sym = reg_to_hack_symbol(dst.value)
                return [f"@{sym}", "M=M-1"]
            out.extend(self.emit_load_operand(src))
            if dst.op_type == OperandType.REGISTER:
                sym = reg_to_hack_symbol(dst.value)
                out.extend([f"@{sym}", "M=M-D"])
            else:
                out.extend(["@__M2H_TMP_VAL", "M=D"])
                out.extend(self.emit_load_operand(dst))
                out.extend(["@__M2H_TMP_VAL", "D=D-M"])
                out.extend(self.emit_store_operand(dst))
            return out

        # 4. and src, dst
        if mn == "and":
            if len(ops) != 2:
                raise ValueError(f"and requires 2 operands, got {len(ops)}")
            src, dst = ops[0], ops[1]
            out.extend(self.emit_load_operand(src))
            if dst.op_type == OperandType.REGISTER:
                sym = reg_to_hack_symbol(dst.value)
                out.extend([f"@{sym}", "M=D&M"])
            else:
                out.extend(["@__M2H_TMP_VAL", "M=D"])
                out.extend(self.emit_load_operand(dst))
                out.extend(["@__M2H_TMP_VAL", "D=D&M"])
                out.extend(self.emit_store_operand(dst))
            return out

        # 5. bis src, dst (Bit Set / OR)
        if mn == "bis":
            if len(ops) != 2:
                raise ValueError(f"bis requires 2 operands, got {len(ops)}")
            src, dst = ops[0], ops[1]
            out.extend(self.emit_load_operand(src))
            if dst.op_type == OperandType.REGISTER:
                sym = reg_to_hack_symbol(dst.value)
                out.extend([f"@{sym}", "M=D|M"])
            else:
                out.extend(["@__M2H_TMP_VAL", "M=D"])
                out.extend(self.emit_load_operand(dst))
                out.extend(["@__M2H_TMP_VAL", "D=D|M"])
                out.extend(self.emit_store_operand(dst))
            return out

        # 6. bic src, dst (Bit Clear: dst = dst & ~src)
        if mn == "bic":
            if len(ops) != 2:
                raise ValueError(f"bic requires 2 operands, got {len(ops)}")
            src, dst = ops[0], ops[1]
            out.extend(self.emit_load_operand(src))
            out.append("D=!D")
            if dst.op_type == OperandType.REGISTER:
                sym = reg_to_hack_symbol(dst.value)
                out.extend([f"@{sym}", "M=D&M"])
            else:
                out.extend(["@__M2H_TMP_VAL", "M=D"])
                out.extend(self.emit_load_operand(dst))
                out.extend(["@__M2H_TMP_VAL", "D=D&M"])
                out.extend(self.emit_store_operand(dst))
            return out

        # 7. xor src, dst (dst = dst ^ src = (src | dst) & ~(src & dst))
        if mn == "xor":
            if len(ops) != 2:
                raise ValueError(f"xor requires 2 operands, got {len(ops)}")
            src, dst = ops[0], ops[1]
            # Load src into __M2H_A, dst into __M2H_B
            out.extend(self.emit_load_operand(src))
            out.extend(["@__M2H_TMP_A", "M=D"])
            out.extend(self.emit_load_operand(dst))
            out.extend(["@__M2H_TMP_B", "M=D"])
            # OR part in __M2H_OR = A | B
            out.extend(["@__M2H_TMP_A", "D=M", "@__M2H_TMP_B", "D=D|M", "@__M2H_TMP_OR", "M=D"])
            # NAND part in __M2H_NAND = !(A & B)
            out.extend(["@__M2H_TMP_A", "D=M", "@__M2H_TMP_B", "D=D&M", "D=!D"])
            # Result = OR & NAND
            out.extend(["@__M2H_TMP_OR", "D=D&M"])
            out.extend(self.emit_store_operand(dst))
            return out

        # 8. clr dst
        if mn == "clr":
            if len(ops) != 1:
                raise ValueError(f"clr requires 1 operand, got {len(ops)}")
            dst = ops[0]
            out.extend(["@0", "D=A"])
            out.extend(self.emit_store_operand(dst))
            return out

        # 9. inc dst
        if mn == "inc":
            if len(ops) != 1:
                raise ValueError(f"inc requires 1 operand, got {len(ops)}")
            dst = ops[0]
            if dst.op_type == OperandType.REGISTER:
                sym = reg_to_hack_symbol(dst.value)
                return [f"@{sym}", "M=M+1"]
            out.extend(self.emit_load_operand(dst))
            out.extend(["D=D+1"])
            out.extend(self.emit_store_operand(dst))
            return out

        # 10. dec dst
        if mn == "dec":
            if len(ops) != 1:
                raise ValueError(f"dec requires 1 operand, got {len(ops)}")
            dst = ops[0]
            if dst.op_type == OperandType.REGISTER:
                sym = reg_to_hack_symbol(dst.value)
                return [f"@{sym}", "M=M-1"]
            out.extend(self.emit_load_operand(dst))
            out.extend(["D=D-1"])
            out.extend(self.emit_store_operand(dst))
            return out

        # 11. inv dst (~dst)
        if mn == "inv":
            if len(ops) != 1:
                raise ValueError(f"inv requires 1 operand, got {len(ops)}")
            dst = ops[0]
            if dst.op_type == OperandType.REGISTER:
                sym = reg_to_hack_symbol(dst.value)
                return [f"@{sym}", "M=!M"]
            out.extend(self.emit_load_operand(dst))
            out.extend(["D=!D"])
            out.extend(self.emit_store_operand(dst))
            return out

        # 12. neg dst (-dst)
        if mn == "neg":
            if len(ops) != 1:
                raise ValueError(f"neg requires 1 operand, got {len(ops)}")
            dst = ops[0]
            if dst.op_type == OperandType.REGISTER:
                sym = reg_to_hack_symbol(dst.value)
                return [f"@{sym}", "M=-M"]
            out.extend(self.emit_load_operand(dst))
            out.extend(["D=-D"])
            out.extend(self.emit_store_operand(dst))
            return out

        # 13. tst dst
        if mn == "tst":
            if len(ops) != 1:
                raise ValueError(f"tst requires 1 operand, got {len(ops)}")
            dst = ops[0]
            out.extend(self.emit_load_operand(dst))
            return out

        # 14. cmp src, dst (dst - src)
        if mn == "cmp":
            if len(ops) != 2:
                raise ValueError(f"cmp requires 2 operands, got {len(ops)}")
            src, dst = ops[0], ops[1]
            out.extend(self.emit_load_operand(src))
            if dst.op_type == OperandType.REGISTER:
                sym = reg_to_hack_symbol(dst.value)
                out.extend([f"@{sym}", "D=M-D"])
            else:
                out.extend(["@__M2H_TMP_VAL", "M=D"])
                out.extend(self.emit_load_operand(dst))
                out.extend(["@__M2H_TMP_VAL", "D=D-M"])
            return out

        # 15. Conditional Jumps (jeq, jz, jne, jnz, jge, jl, jn, jmp)
        if mn in ("jeq", "jz"):
            if len(ops) != 1:
                raise ValueError(f"{mn} requires 1 target operand")
            target = sanitize_symbol(ops[0].value)
            return [f"@{target}", "D;JEQ"]

        if mn in ("jne", "jnz"):
            if len(ops) != 1:
                raise ValueError(f"{mn} requires 1 target operand")
            target = sanitize_symbol(ops[0].value)
            return [f"@{target}", "D;JNE"]

        if mn == "jge":
            if len(ops) != 1:
                raise ValueError("jge requires 1 target operand")
            target = sanitize_symbol(ops[0].value)
            return [f"@{target}", "D;JGE"]

        if mn in ("jl", "jn"):
            if len(ops) != 1:
                raise ValueError(f"{mn} requires 1 target operand")
            target = sanitize_symbol(ops[0].value)
            return [f"@{target}", "D;JLT"]

        if mn == "jmp":
            if len(ops) != 1:
                raise ValueError("jmp requires 1 target operand")
            target = sanitize_symbol(ops[0].value)
            return [f"@{target}", "0;JMP"]

        # 16. push src
        if mn == "push":
            if len(ops) != 1:
                raise ValueError("push requires 1 operand")
            src = ops[0]
            out.extend(self.emit_load_operand(src))
            out.extend(["@SP", "A=M", "M=D", "@SP", "M=M+1"])
            return out

        # 17. pop dst
        if mn == "pop":
            if len(ops) != 1:
                raise ValueError("pop requires 1 operand")
            dst = ops[0]
            out.extend(["@SP", "M=M-1", "A=M", "D=M"])
            out.extend(self.emit_store_operand(dst))
            return out

        # 18. call fn
        if mn == "call":
            if len(ops) != 1:
                raise ValueError("call requires 1 target operand")
            fn_target = sanitize_symbol(ops[0].value)
            ret_lbl = self.next_return_label()
            return [
                f"@{ret_lbl}",
                "D=A",
                "@SP",
                "A=M",
                "M=D",
                "@SP",
                "M=M+1",
                f"@{fn_target}",
                "0;JMP",
                f"({ret_lbl})",
            ]

        # 19. ret
        if mn == "ret":
            return ["@SP", "M=M-1", "A=M", "A=M", "0;JMP"]

        # 20. nop
        if mn == "nop":
            return ["// nop"]

        raise ValueError(f"Unsupported mnemonic: '{mn}' on line {stmt.line_number}")

    def emit_program(self, statements: list[Statement]) -> str:
        """Transpile a list of Statements into a complete Hack assembly program."""
        lines: list[str] = []

        if self.include_crt0:
            from m2h.crt0 import generate_crt0

            lines.extend(generate_crt0())
            lines.append("")

        for stmt in statements:
            emitted = self.emit_statement(stmt)
            if emitted:
                lines.extend(emitted)

        return "\n".join(lines) + "\n"
