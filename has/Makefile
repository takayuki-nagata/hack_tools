objects = main.o assembler.o parser.o code.o symbol_table.o output_formatter.o
program = has

all: has
clean:
	rm $(objects)

$(objects): %.o: %.c
	$(CC) -c $(CFLAGS) $< -o $@

$(program): $(objects)
	$(CC) $(objects) -o $@

.PHONY: clean
