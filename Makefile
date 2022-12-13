IPYNB_SOURCES := $(wildcard src/*.md)
IPYNBS := $(patsubst src/%.md, %.ipynb, $(IPYNB_SOURCES))

.PHONY: all clean release test

all: $(IPYNBS)

%.ipynb: src/%.md
	pandoc $< -o $@

release:
	@echo "Release not yet implemented!"

test:
	@echo "Tests not yet implemented!"

clean:
	rm -f $(IPYNBS)
