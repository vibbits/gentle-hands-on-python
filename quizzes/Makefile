SOURCE_FORMAT="markdown_strict+pipe_tables+backtick_code_blocks+auto_identifiers+strikeout+yaml_metadata_block+implicit_figures+all_symbols_escapable+link_attributes+smart+fenced_divs+fancy_lists"

SOURCES := $(wildcard *.md)
PDFS = $(SOURCES:.md=.pdf)

%.pdf: %.md
	@echo "Compiling "$@
	@pandoc -s --listings --template default_mod.latex --pdf-engine xelatex -f $(SOURCE_FORMAT) -t beamer $< -o $@

.PHONY: all clean

all: $(PDFS)

clean:
	rm -f $(PDFS)
