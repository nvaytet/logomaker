import argparse
import subprocess
import tempfile
from pathlib import Path


def main(prefix: str, suffix: str, footer: str, output: str, color: str):
    template = Path(__file__).resolve().parent.joinpath("template.svg").read_text()
    out = template.format(prefix=prefix, suffix=suffix, footer=footer, color=color)
    with tempfile.NamedTemporaryFile(mode="w", suffix=".svg", delete=False) as f:
        fname = f.name
        Path(fname).write_text(out)
        subprocess.run(
            [
                "inkscape",
                "--actions=page-fit-to-selection;export-text-to-path",
                "-o",
                output,
                fname,
            ]
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prefix", type=str)
    parser.add_argument("--suffix", type=str, default="")
    parser.add_argument("--footer", type=str, default="")
    parser.add_argument("--output", type=str, default="logo.svg")
    parser.add_argument("--color", type=str, default="#0065ac")
    args = parser.parse_args()
    main(
        prefix=args.prefix,
        suffix=args.suffix,
        footer=args.footer,
        output=args.output,
        color=args.color,
    )
