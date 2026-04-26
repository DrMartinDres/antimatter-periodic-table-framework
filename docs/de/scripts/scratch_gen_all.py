import os


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT_DIR, "paper")
CELL = "0.68cm"
MIRROR_SHIFT = 10.0

LEGEND_BOX_H = 0.30
LEGEND_ROW_DY = 0.70
LEGEND_Y0 = -10.20

# Element data: (Z, Symbol, Period, Group). The main block uses the 18-column
# layout; lanthanides and actinides are shown as separated f-block rows.
elements = [
    (1, "H", 1, 1), (2, "He", 1, 18),
    (3, "Li", 2, 1), (4, "Be", 2, 2), (5, "B", 2, 13), (6, "C", 2, 14), (7, "N", 2, 15), (8, "O", 2, 16), (9, "F", 2, 17), (10, "Ne", 2, 18),
    (11, "Na", 3, 1), (12, "Mg", 3, 2), (13, "Al", 3, 13), (14, "Si", 3, 14), (15, "P", 3, 15), (16, "S", 3, 16), (17, "Cl", 3, 17), (18, "Ar", 3, 18),
    (19, "K", 4, 1), (20, "Ca", 4, 2), (21, "Sc", 4, 3), (22, "Ti", 4, 4), (23, "V", 4, 5), (24, "Cr", 4, 6), (25, "Mn", 4, 7), (26, "Fe", 4, 8), (27, "Co", 4, 9), (28, "Ni", 4, 10), (29, "Cu", 4, 11), (30, "Zn", 4, 12), (31, "Ga", 4, 13), (32, "Ge", 4, 14), (33, "As", 4, 15), (34, "Se", 4, 16), (35, "Br", 4, 17), (36, "Kr", 4, 18),
    (37, "Rb", 5, 1), (38, "Sr", 5, 2), (39, "Y", 5, 3), (40, "Zr", 5, 4), (41, "Nb", 5, 5), (42, "Mo", 5, 6), (43, "Tc", 5, 7), (44, "Ru", 5, 8), (45, "Rh", 5, 9), (46, "Pd", 5, 10), (47, "Ag", 5, 11), (48, "Cd", 5, 12), (49, "In", 5, 13), (50, "Sn", 5, 14), (51, "Sb", 5, 15), (52, "Te", 5, 16), (53, "I", 5, 17), (54, "Xe", 5, 18),
    (55, "Cs", 6, 1), (56, "Ba", 6, 2), (71, "Lu", 6, 3), (72, "Hf", 6, 4), (73, "Ta", 6, 5), (74, "W", 6, 6), (75, "Re", 6, 7), (76, "Os", 6, 8), (77, "Ir", 6, 9), (78, "Pt", 6, 10), (79, "Au", 6, 11), (80, "Hg", 6, 12), (81, "Tl", 6, 13), (82, "Pb", 6, 14), (83, "Bi", 6, 15), (84, "Po", 6, 16), (85, "At", 6, 17), (86, "Rn", 6, 18),
    (87, "Fr", 7, 1), (88, "Ra", 7, 2), (103, "Lr", 7, 3), (104, "Rf", 7, 4), (105, "Db", 7, 5), (106, "Sg", 7, 6), (107, "Bh", 7, 7), (108, "Hs", 7, 8), (109, "Mt", 7, 9), (110, "Ds", 7, 10), (111, "Rg", 7, 11), (112, "Cn", 7, 12), (113, "Nh", 7, 13), (114, "Fl", 7, 14), (115, "Mc", 7, 15), (116, "Lv", 7, 16), (117, "Ts", 7, 17), (118, "Og", 7, 18),
]

lanthanides = [(Z, sym, 8.5, col) for Z, sym, col in zip(range(57, 71), ["La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb"], range(4, 18))]
actinides = [(Z, sym, 9.5, col) for Z, sym, col in zip(range(89, 103), ["Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No"], range(4, 18))]
all_elements = elements + lanthanides + actinides


def block_color(col, row):
    if col in [1, 2]:
        return "blue!18"
    if col >= 13:
        return "green!18"
    if 3 <= col <= 12 and row <= 7:
        return "orange!20"
    return "red!18"


def status_color(z):
    if z == 1:
        return "green!60"
    if z == 2:
        return "orange!60"
    return "gray!8"


def evidence_marker(z):
    if z == 1:
        return "="
    if z == 2:
        return "K"
    return "?"


def anti_symbol(sym):
    return rf"$\overline{{\mathrm{{{sym}}}}}$"


def write_file(name, text):
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, name), "w", encoding="utf-8") as f:
        f.write(text)


def tikz_begin(extra=""):
    return rf"\begin{{tikzpicture}}[x={CELL}, y={CELL}, every node/.style={{inner sep=0pt}}{extra}]" + "\n"


def fixed_bbox(x0, y0, x1, y1):
    # Forces identical horizontal anchoring across figures by fixing the TikZ bounding box.
    return rf"\path[use as bounding box] ({x0},{y0}) rectangle ({x1},{y1});" + "\n"


def legend_block(x, y, color, text):
    return rf"""\draw[fill={color}, draw=black] ({x},{y}) rectangle ({x + 0.55},{y - {LEGEND_BOX_H}});
\node[anchor=west] at ({x + 0.70},{y - 0.15}) {{\scriptsize {text}}};
"""


def standard_cell(z, sym, x, y, color):
    return rf"""\draw[fill={color}, draw=black, rounded corners=0.7pt] ({x},{y}) rectangle ({x+1},{y-1});
\node at ({x+0.52},{y-0.46}) {{\scriptsize \textbf{{{sym}}}}};
\node at ({x+0.18},{y-0.18}) {{\tiny {z}}};
"""


def legend_label(x, y, text):
    return rf"\node[anchor=west] at ({x},{y}) {{\scriptsize \textbf{{{text}}}}};" + "\n"


def legend_square(x, y, color, text):
    y2 = y - LEGEND_BOX_H
    return rf"""\draw[fill={color}, draw=black] ({x},{y}) rectangle ({x + 0.55},{y2});
\node[anchor=west] at ({x + 0.70},{y - 0.15}) {{\scriptsize {text}}};
"""


def legend_block_row(y, x0=0.0):
    tex = legend_label(x0, y - 0.11, "Block:")
    x = x0 + 1.65
    tex += legend_square(x, y, "blue!18", "s")
    x += 1.20
    tex += legend_square(x, y, "green!18", "p")
    x += 1.20
    tex += legend_square(x, y, "orange!20", "d")
    x += 1.20
    tex += legend_square(x, y, "red!18", "f")
    return tex


def legend_cellsize_row(y, x=7.4):
    return rf"\node[anchor=west] at ({x},{y - 0.15}) {{\scriptsize Elementzellen: $0.68\,\mathrm{{cm}}\times0.68\,\mathrm{{cm}}$.}};" + "\n"


def legend_marker_row(y, x=0.0):
    tex = legend_label(x, y - 0.11, "Marker:")
    tex += rf"\node[anchor=west] at ({x + 2.2},{y - 0.15}) {{\scriptsize $=$ CPT-kompatibel;\quad K Antikern;\quad ? offen;\quad R Residual.}};" + "\n"
    return tex


def legend_anticolor_row(y, x=0.0):
    tex = legend_label(x, y - 0.11, "Anti-Farbe:")
    x2 = x + 2.2
    tex += legend_square(x2, y, "green!60", "Atom")
    x2 += 2.0
    tex += legend_square(x2, y, "orange!60", "Kern")
    x2 += 2.0
    tex += legend_square(x2, y, "gray!8", "offen")
    return tex


def standard_table():
    tex = "\\begin{figure}[p]\n\\centering\n" + tikz_begin()
    tex += fixed_bbox(0, 0.1, 18, -11.6)
    for z, sym, row, col in all_elements:
        tex += standard_cell(z, sym, col - 1, -row + 1, block_color(col, row))
    tex += legend_block_row(LEGEND_Y0)
    tex += legend_cellsize_row(LEGEND_Y0, x=7.4)
    tex += r"""\end{tikzpicture}
\caption{Variante 0: Klassisches Periodensystem als Referenz. Die Farben kodieren nur die Orbitalblock-Struktur der Materie; alle Elementzellen besitzen dieselbe physische Groesse wie in den folgenden Periodentafeln.}
\label{fig:ptable-standard}
\end{figure}
"""
    return tex


def split_cell_table():
    tex = "\\begin{figure}[p]\n\\centering\n" + tikz_begin()
    tex += fixed_bbox(0, 0.1, 18, -12.2)
    for z, sym, row, col in all_elements:
        x = col - 1
        y = -row + 1
        marker = evidence_marker(z)
        tex += rf"""\fill[{block_color(col, row)}, rounded corners=0.7pt] ({x},{y}) -- ({x+1},{y}) -- ({x+1},{y-1}) -- cycle;
\fill[{status_color(z)}, rounded corners=0.7pt] ({x},{y}) -- ({x},{y-1}) -- ({x+1},{y-1}) -- cycle;
\draw[black, rounded corners=0.7pt] ({x},{y}) rectangle ({x+1},{y-1});
\draw[black, dashed, very thin] ({x},{y}) -- ({x+1},{y-1});
\node at ({x+0.70},{y-0.25}) {{\tiny \textbf{{{sym}}}}};
\node at ({x+0.28},{y-0.73}) {{\tiny \textbf{{{anti_symbol(sym)}}}}};
\node at ({x+0.18},{y-0.18}) {{\tiny {z}}};
\node[fill=white, draw=black, circle, inner sep=0.4pt] at ({x+0.80},{y-0.80}) {{\tiny \textbf{{{marker}}}}};
"""
    tex += "\n"
    tex += legend_block_row(LEGEND_Y0)
    tex += legend_cellsize_row(LEGEND_Y0, x=7.4)
    tex += legend_marker_row(LEGEND_Y0 - LEGEND_ROW_DY)
    tex += legend_anticolor_row(LEGEND_Y0 - 2 * LEGEND_ROW_DY)
    tex += r"""\end{tikzpicture}
\caption{Variante A: Split-Cell-Antiperiodensystem. Jede Zelle trennt die bekannte Orbitalblock-Struktur von der empirischen Antimaterie-Evidenz; der Marker zeigt, ob Gleichheit gemessen ($=$), nur ein Antikern bekannt (K), das Anti-Atom offen (?) oder ein Residualfall zu analysieren ist (R).}
\label{fig:ptable-split}
\end{figure}
"""
    return tex


def mirrored_table():
    tex = "\\begin{figure}[p]\n\\centering\n" + tikz_begin()
    # The mirrored table has a lower (evidence) half reaching down to y=-MIRROR_SHIFT-1.
    # Place the legend safely below that to avoid collisions.
    legend_y0 = -MIRROR_SHIFT - 1.4
    bbox_bottom = legend_y0 - 2 * LEGEND_ROW_DY - LEGEND_BOX_H - 0.8
    tex += fixed_bbox(0, MIRROR_SHIFT + 0.2, 18, bbox_bottom)
    for z, sym, row, col in all_elements:
        x = col - 1
        y = -row + 1 + MIRROR_SHIFT
        tex += standard_cell(z, sym, x, y, block_color(col, row))
    tex += r"""\draw[line width=1.2pt, dashed, red!70!black] (0,0) -- (18,0);
\node[red!70!black, anchor=west] at (0.2,0.25) {\scriptsize Ladungskonjugation; $Z$ bleibt positiver Tabellenindex};
"""
    for z, sym, row, col in all_elements:
        x = col - 1
        y = row - 1 - MIRROR_SHIFT
        tex += rf"""\draw[fill={status_color(z)}, draw=black, rounded corners=0.7pt] ({x},{y}) rectangle ({x+1},{y-1});
\node at ({x+0.52},{y-0.42}) {{\tiny \textbf{{{anti_symbol(sym)}}}}};
\node at ({x+0.18},{y-0.82}) {{\tiny {z}}};
\node[fill=white, draw=black, circle, inner sep=0.4pt] at ({x+0.82},{y-0.82}) {{\tiny \textbf{{{evidence_marker(z)}}}}};
"""
    tex += "\n"
    tex += legend_block_row(legend_y0)
    tex += legend_cellsize_row(legend_y0, x=7.4)
    tex += legend_marker_row(legend_y0 - LEGEND_ROW_DY)
    tex += legend_anticolor_row(legend_y0 - 2 * LEGEND_ROW_DY)
    tex += r"""\end{tikzpicture}
\caption{Variante B: Duales gespiegeltes Periodensystem. Die Antimaterie-Haelfte ist eine Evidenzkarte mit derselben Elementzellgroesse wie die Referenz- und Split-Cell-Tafel.}
\label{fig:ptable-mirrored}
\end{figure}
"""
    return tex


def asymmetry_map():
    return r"""
\begin{figure}[H]
\centering
\small
\setlength{\tabcolsep}{4pt}
\renewcommand{\arraystretch}{1.25}
\begin{tabular}{L{0.20\textwidth}L{0.18\textwidth}L{0.20\textwidth}L{0.18\textwidth}L{0.18\textwidth}}
\toprule
\textbf{Observable} & \textbf{links: $\rho_O<0$} & \textbf{Diagonale: $\rho_O\simeq0$} & \textbf{rechts: $\rho_O>0$} & \textbf{unmeasured / Status}\\
\midrule
$m/q$ & -- & \cellcolor{green!45}$\anti{H}$ / $\bar p$ kompatibel & -- & \cellcolor{orange!35}$\anti{He}$: K; $Z\geq3$: ?\\
$1S$--$2S$ & -- & \cellcolor{green!45}$\anti{H}[1S\text{--}2S:0]$ & -- & \cellcolor{gray!8}$Z\geq2$: ?\\
$g$ & -- & \cellcolor{green!45}$\anti{H}[g:0]$ & -- & \cellcolor{gray!8}$Z\geq2$: ?\\
Chemie & -- & -- & -- & \cellcolor{yellow!35}theoretisch vorbereitet / ?\\
Kosmische Suche & -- & -- & -- & \cellcolor{yellow!35}Suchraum, keine Anti-Atom-Chemie\\
\bottomrule
\end{tabular}

\vspace{0.45em}
\scriptsize
Diagonal bedeutet CPT-kompatibel innerhalb Unsicherheit. Links/rechts werden erst verwendet, wenn ein signifikantes negatives/positives Residuum gemessen wird. Fehlende Daten bleiben als ? oder K markiert und werden nicht als Abweichung interpretiert.
\caption{Variante C: Diagonal- und Residualschema fuer moegliche Materie-Antimaterie-Asymmetrien. Gleichheit liegt auf der Diagonalen; signifikante Abweichungen wuerden nach links oder rechts verschoben, waehrend unbekannte Anti-Systeme separat als ungemessen markiert bleiben.}
\label{fig:asymmetry-map}
\end{figure}
"""


write_file("ptable_standard.tex", standard_table())
write_file("ptable_epistemic_revised.tex", split_cell_table())
write_file("ptable_split.tex", split_cell_table())
write_file("ptable_mirrored.tex", mirrored_table())
write_file("ptable_asymmetry.tex", asymmetry_map())
print("generated ptable_standard.tex, ptable_epistemic_revised.tex, ptable_split.tex, ptable_mirrored.tex, ptable_asymmetry.tex")
