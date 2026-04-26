import os
import shutil
import subprocess
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
PAPER_DIR = ROOT_DIR / "paper"
FIGURES_DIR = ROOT_DIR / "figures"
TMP_DIR = ROOT_DIR / "tmp" / "pdfs"
LEGACY_TECTONIC = Path(
    "/Users/martindres/.gemini/antigravity/brain/b891fbf2-924c-4580-a462-49df42b1b7c7/scratch/tectonic"
)

FIGURES = {
    "periodic_table_reference": "ptable_standard.tex",
    "antimatter_periodic_table_status": "ptable_epistemic_revised.tex",
    "split_cell_representation": "ptable_split.tex",
    "deviation_model": "ptable_asymmetry.tex",
    "antinuclide_mapping": "ptable_mirrored.tex",
}

PREAMBLE = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[english]{babel}
\usepackage{lmodern}
\usepackage[a4paper,margin=1.2cm]{geometry}
\usepackage{amsmath,amssymb,mathtools}
\usepackage{booktabs,array,longtable}
\usepackage[table]{xcolor}
\usepackage{graphicx}
\usepackage{tikz}
\usepackage{pdflscape}
\usepackage{float}
\usepackage{caption}
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
\newcommand{\anti}[1]{\ensuremath{\overline{\mathrm{#1}}}}
\pagestyle{empty}
\begin{document}
"""

POSTAMBLE = r"""
\end{document}
"""


def main() -> None:
    tectonic = shutil.which("tectonic")
    if tectonic is None and LEGACY_TECTONIC.exists():
        tectonic = str(LEGACY_TECTONIC)
    if tectonic is None:
        raise SystemExit("Tectonic not found. Install tectonic or add it to PATH.")

    FIGURES_DIR.mkdir(exist_ok=True)
    TMP_DIR.mkdir(parents=True, exist_ok=True)

    for output_name, input_name in FIGURES.items():
        wrapper = TMP_DIR / f"{output_name}.tex"
        input_path = os.path.relpath(PAPER_DIR / input_name, TMP_DIR)
        wrapper.write_text(PREAMBLE + f"\\input{{{input_path}}}\n" + POSTAMBLE, encoding="utf-8")

        subprocess.run([tectonic, wrapper.name], cwd=TMP_DIR, check=True)
        shutil.copy2(TMP_DIR / f"{output_name}.pdf", FIGURES_DIR / f"{output_name}.pdf")

    print("built " + ", ".join(f"{name}.pdf" for name in FIGURES))


if __name__ == "__main__":
    main()
