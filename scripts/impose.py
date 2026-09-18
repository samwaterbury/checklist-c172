"""Arrange four half-Letter pages on one duplex Letter sheet, without scaling."""
import argparse
from pathlib import Path

from pypdf import PdfReader, PdfWriter, Transformation


def impose(source, destination):
    reader = PdfReader(source)
    if len(reader.pages) != 4:
        raise ValueError("Letter printing requires exactly four half-Letter pages")
    for page in reader.pages:
        if (tuple(float(v) for v in page.mediabox) != (0, 0, 396, 612)
                or tuple(page.cropbox) != tuple(page.mediabox) or page.rotation != 0):
            raise ValueError("Letter printing requires unrotated 5.5 x 8.5 inch pages")

    writer = PdfWriter()
    # Front: 1 | 3. Back: 4 | 2. Landscape, short-edge duplex, center cut.
    for pair in ((0, 2), (3, 1)):
        sheet = writer.add_blank_page(width=792, height=612)
        for half, index in enumerate(pair):
            sheet.merge_transformed_page(
                reader.pages[index], Transformation().translate(tx=396 * half),
            )
    writer.add_metadata({
        "/Title": "Cessna 172S G1000 Checklist - Letter printing",
        "/Subject": "Print at 100%, landscape, duplex short edge; cut at 5.5 inches.",
    })
    writer.create_viewer_preferences()
    writer.viewer_preferences.print_scaling = "/None"
    writer.viewer_preferences.duplex = "/DuplexFlipShortEdge"
    # Keep a previous valid output intact if writing fails.
    destination = Path(destination)
    temporary = destination.with_suffix(".tmp.pdf")
    try:
        writer.write(temporary)
        temporary.replace(destination)
    finally:
        temporary.unlink(missing_ok=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    if args.source.resolve() == args.destination.resolve():
        parser.error("Source and destination must be different files")
    impose(args.source, args.destination)
