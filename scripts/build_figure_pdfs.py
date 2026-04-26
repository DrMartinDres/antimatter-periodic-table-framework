import base64
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

FULLSIZE_SPLIT_CELL = "split_cell_table_v1.0.0"

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

FULLSIZE_PREAMBLE = PREAMBLE.replace(
    r"\usepackage[a4paper,margin=1.2cm]{geometry}",
    r"\usepackage[a3paper,landscape,margin=1.2cm]{geometry}",
)

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
    paper_input_path = os.path.relpath(PAPER_DIR, TMP_DIR).replace(os.sep, "/")
    input_search_path = f"\\makeatletter\\def\\input@path{{{{{paper_input_path}/}}}}\\makeatother\n"

    for output_name, input_name in FIGURES.items():
        wrapper = TMP_DIR / f"{output_name}.tex"
        input_path = os.path.relpath(PAPER_DIR / input_name, TMP_DIR)
        wrapper.write_text(
            PREAMBLE + input_search_path + f"\\input{{{input_path}}}\n" + POSTAMBLE,
            encoding="utf-8",
        )

        subprocess.run([tectonic, wrapper.name], cwd=TMP_DIR, check=True)
        shutil.copy2(TMP_DIR / f"{output_name}.pdf", FIGURES_DIR / f"{output_name}.pdf")

    core_input_path = os.path.relpath(PAPER_DIR / "ptable_split_core.tex", TMP_DIR)
    core_wrapper = TMP_DIR / f"{FULLSIZE_SPLIT_CELL}.tex"
    core_wrapper.write_text(
        FULLSIZE_PREAMBLE
        + input_search_path
        + f"\\begin{{center}}\\input{{{core_input_path}}}\\end{{center}}\n"
        + POSTAMBLE,
        encoding="utf-8",
    )
    subprocess.run([tectonic, core_wrapper.name], cwd=TMP_DIR, check=True)

    split_pdf = TMP_DIR / f"{FULLSIZE_SPLIT_CELL}.pdf"
    export_pdf = split_pdf
    pdfcrop = shutil.which("pdfcrop")
    if pdfcrop is not None:
        cropped_pdf = TMP_DIR / f"{FULLSIZE_SPLIT_CELL}.pdf"
        uncropped_pdf = TMP_DIR / f"{FULLSIZE_SPLIT_CELL}-uncropped.pdf"
        shutil.move(split_pdf, uncropped_pdf)
        subprocess.run([pdfcrop, "--margins", "8", str(uncropped_pdf), str(cropped_pdf)], check=True)
        export_pdf = cropped_pdf
    shutil.copy2(export_pdf, FIGURES_DIR / f"{FULLSIZE_SPLIT_CELL}.pdf")

    try:
        import pypdfium2 as pdfium

        pdf = pdfium.PdfDocument(str(export_pdf))
        bitmap = pdf[0].render(scale=4.0)
        image = bitmap.to_pil()
        png_path = FIGURES_DIR / f"{FULLSIZE_SPLIT_CELL}.png"
        svg_path = FIGURES_DIR / f"{FULLSIZE_SPLIT_CELL}.svg"
        image.save(png_path)
        encoded_png = base64.b64encode(png_path.read_bytes()).decode("ascii")
        svg_path.write_text(
            (
                "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
                f"<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"{image.width}\" "
                f"height=\"{image.height}\" viewBox=\"0 0 {image.width} {image.height}\">\n"
                f"  <image width=\"{image.width}\" height=\"{image.height}\" "
                f"href=\"data:image/png;base64,{encoded_png}\"/>\n"
                "</svg>\n"
            ),
            encoding="utf-8",
        )
    except Exception as exc:
        print(f"skipped PNG/SVG export: {exc}")

    built = [f"{name}.pdf" for name in FIGURES]
    built.extend(
        [
            f"{FULLSIZE_SPLIT_CELL}.pdf",
            f"{FULLSIZE_SPLIT_CELL}.svg",
            f"{FULLSIZE_SPLIT_CELL}.png",
        ]
    )
    print("built " + ", ".join(built))


if __name__ == "__main__":
    main()
