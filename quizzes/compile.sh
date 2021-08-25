#!/usr/bin/bash

DATE_COVER=$(date "+%d %B %Y")

SOURCE_FORMAT="markdown_strict\
+pipe_tables\
+backtick_code_blocks\
+auto_identifiers\
+strikeout\
+yaml_metadata_block\
+implicit_figures\
+all_symbols_escapable\
+link_attributes\
+smart\
+fenced_divs"

FILES="day1_after_lunch day1_end day2_intro day2_morning_break day2_after_lunch day2_afternoon"

for name in ${FILES}; do
    echo "Compiling ${name}.pdf"
    pandoc -s --listings --template default_mod.latex --pdf-engine xelatex -f "$SOURCE_FORMAT" -t beamer ${name}.md -o ${name}.pdf
done
