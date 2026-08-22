# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2026 Takayuki Nagata

import sys

from m2h.cli import main

if __name__ == "__main__":
    sys.exit(main())


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
