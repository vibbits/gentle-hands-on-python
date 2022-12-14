IPYNB_SOURCES := $(wildcard src/*.md)
IPYNBS := $(patsubst src/%.md, %.ipynb, $(IPYNB_SOURCES))
DATA_FILES := data/HadCRUT.5.0.1.0.analysis.summary_series.global.monthly.csv data/readfile.txt
PROJECTS := projects/Index.ipynb projects/sequence_assembly.ipynb projects/image_segmentation.ipynb projects/3d_protein_structure.ipynb
IMAGES := images/blast_results.png images/blast_search.png images/fizzbuzz_flowchart.svg images/function.png images/global_climate_plot.png images/hedy_1.png images/hedy_2.png images/hedy_3.png images/hedy_4.png images/hedy_next_level.png images/hedy_run_code.png images/myDictionary-cropped.png images/sequence_assembly_solution.png images/testing.png

.PHONY: all clean release test

all: $(IPYNBS) release

%.ipynb: src/%.md
	pandoc $< -o $@

release: materials.zip

materials.zip: $(IPYNBS)
	zip -r materials.zip Revision.ipynb 00_Python_Cheat_Sheet.ipynb solutions/Solutions.ipynb Advanced\ Exercises.ipynb projects/images/ projects/solutions/ $(IPYNBS) $(DATA_FILES) $(IMAGES) $(PROJECTS)

test:
	@echo "Tests not yet implemented!"

clean:
	rm -rf $(IPYNBS) __pycache__/ projects/__pycache__/ projects/solutions/__pycache__/ projects/solutions/.mypy_cache/ projects/solutions/.ipynb_checkpoints/ projects/solutions/sa/__pycache__/ images/.ipynb_checkpoints/
	git clean -f
