PYTHON ?= python3

.PHONY: build watch
build:
	mkdir -p output/pdf
	./scripts/typst compile main.typ output/pdf/checklist.pdf
	$(PYTHON) scripts/impose.py output/pdf/checklist.pdf output/pdf/checklist-letter.pdf

watch:
	mkdir -p output/pdf
	./scripts/typst watch main.typ output/pdf/checklist.pdf
