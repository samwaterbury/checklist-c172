# C172S G1000 checklist

These are my checklists for the Cessna 172S G1000.

## Build

1. Install [Typst 0.15.1](https://github.com/typst/typst/releases/tag/v0.15.1)
2. Ensure Helvetica Neue and Helvetica are available
3. Install the Python dependency and build:

```sh
python3 -m venv .tools/venv
.tools/venv/bin/pip install -r requirements.txt
make build PYTHON=.tools/venv/bin/python
```

Outputs are `output/pdf/checklist.pdf` (four half-Letter pages) and `output/pdf/checklist-letter.pdf` (two landscape Letter sides). Print the Letter version at **100%, double-sided, flip on short edge**, then cut in half for one complete set.

## Development

Edit checklist content in `content/procedures.yaml`, placement in `layout/kneeboard.yaml`, and styling in `theme.typ`.

`make watch` previews changes in the half-Letter PDF; run `make build` with your Python environment to refresh both outputs.

See [AGENTS.md](AGENTS.md) for maintenance notes and references.
