# C172S G1000 checklist

These are my checklists for the Cessna 172S G1000.

## Build

1. Install [Typst 0.15.1](https://github.com/typst/typst/releases/tag/v0.15.1)
2. Ensure Helvetica Neue and Helvetica are available
3. Run `make build` to generate outputs

## Development

Edit checklist content in `content/procedures.yaml`, placement in `layout/kneeboard.yaml`, and styling in `theme.typ`.

```sh
python3 -m venv .tools/test-venv
.tools/test-venv/bin/pip install -r requirements-dev.txt
make test PYTHON=.tools/test-venv/bin/python
```

See [AGENTS.md](AGENTS.md) for maintenance notes and references.
