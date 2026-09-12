PYTHON ?= python3

.PHONY: build watch test
build:
	mkdir -p output/pdf
	./scripts/typst compile main.typ output/pdf/checklist.pdf

watch:
	mkdir -p output/pdf
	./scripts/typst watch main.typ output/pdf/checklist.pdf

test:
	$(PYTHON) -m unittest discover -s tests -v
