import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT_DIR, "paper")

elements = [
    (1, "H", 1, 1), (2, "He", 1, 18),
    (3, "Li", 2, 1), (4, "Be", 2, 2), (5, "B", 2, 13), (6, "C", 2, 14), (7, "N", 2, 15), (8, "O", 2, 16), (9, "F", 2, 17), (10, "Ne", 2, 18),
    (11, "Na", 3, 1), (12, "Mg", 3, 2), (13, "Al", 3, 13), (14, "Si", 3, 14), (15, "P", 3, 15), (16, "S", 3, 16), (17, "Cl", 3, 17), (18, "Ar", 3, 18),
    (19, "K", 4, 1), (20, "Ca", 4, 2), (21, "Sc", 4, 3), (22, "Ti", 4, 4), (23, "V", 4, 5), (24, "Cr", 4, 6), (25, "Mn", 4, 7), (26, "Fe", 4, 8), (27, "Co", 4, 9), (28, "Ni", 4, 10), (29, "Cu", 4, 11), (30, "Zn", 4, 12), (31, "Ga", 4, 13), (32, "Ge", 4, 14), (33, "As", 4, 15), (34, "Se", 4, 16), (35, "Br", 4, 17), (36, "Kr", 4, 18),
    (37, "Rb", 5, 1), (38, "Sr", 5, 2), (39, "Y", 5, 3), (40, "Zr", 5, 4), (41, "Nb", 5, 5), (42, "Mo", 5, 6), (43, "Tc", 5, 7), (44, "Ru", 5, 8), (45, "Rh", 5, 9), (46, "Pd", 5, 10), (47, "Ag", 5, 11), (48, "Cd", 5, 12), (49, "In", 5, 13), (50, "Sn", 5, 14), (51, "Sb", 5, 15), (52, "Te", 5, 16), (53, "I", 5, 17), (54, "Xe", 5, 18),
    (55, "Cs", 6, 1), (56, "Ba", 6, 2), (71, "Lu", 6, 3), (72, "Hf", 6, 4), (73, "Ta", 6, 5), (74, "W", 6, 6), (75, "Re", 6, 7), (76, "Os", 6, 8), (77, "Ir", 6, 9), (78, "Pt", 6, 10), (79, "Au", 6, 11), (80, "Hg", 6, 12), (81, "Tl", 6, 13), (82, "Pb", 6, 14), (83, "Bi", 6, 15), (84, "Po", 6, 16), (85, "At", 6, 17), (86, "Rn", 6, 18),
    (87, "Fr", 7, 1), (88, "Ra", 7, 2), (103, "Lr", 7, 3), (104, "Rf", 7, 4), (105, "Db", 7, 5), (106, "Sg", 7, 6), (107, "Bh", 7, 7), (108, "Hs", 7, 8), (109, "Mt", 7, 9), (110, "Ds", 7, 10), (111, "Rg", 7, 11), (112, "Cn", 7, 12), (113, "Nh", 7, 13), (114, "Fl", 7, 14), (115, "Mc", 7, 15), (116, "Lv", 7, 16), (117, "Ts", 7, 17), (118, "Og", 7, 18)
]

# Lanth/Actinides placed below
lanthanides = [(Z, sym, 8, col) for Z, sym, col in zip(range(57, 71), ["La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb"], range(4, 18))]
actinides = [(Z, sym, 9, col) for Z, sym, col in zip(range(89, 103), ["Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No"], range(4, 18))]

elements.extend(lanthanides)
elements.extend(actinides)

def get_color(Z):
    if Z == 1:
        return "green!40"
    elif Z >= 104:
        return "gray!40"
    else:
        return "cyan!40"

tex_code = r"""
\begin{figure}[h]
\centering
\resizebox{\textwidth}{!}{
\begin{tikzpicture}[x=1.1cm, y=1.1cm]
"""

for Z, sym, row, col in elements:
    color = get_color(Z)
    x = col - 1
    y = -row + 1
    
    # Render with overline to signify antimatter
    antisym = rf"$\overline{{\mathrm{{{sym}}}}}$"
    
    tex_code += rf"""\draw[fill={color}, draw=black, thick, rounded corners=1pt] ({x},{y}) rectangle ({x+1},{y-1});
\node at ({x+0.5},{y-0.4}) {{\large \textbf{{{antisym}}}}};
\node at ({x+0.2},{y-0.15}) {{\tiny {Z}}};
"""

tex_code += r"""
\node at (2, -1) {\textbf{Level 1: Confirmed}};
\draw[fill=green!40, draw=black, thick, rounded corners=1pt] (4.5,-0.7) rectangle (5.5,-1.3);

\node at (2, -2) {\textbf{Level 2: Expected}};
\draw[fill=cyan!40, draw=black, thick, rounded corners=1pt] (4.5,-1.7) rectangle (5.5,-2.3);

\node at (2, -3) {\textbf{Level 3: Open Domain}};
\draw[fill=gray!40, draw=black, thick, rounded corners=1pt] (4.5,-2.7) rectangle (5.5,-3.3);

\end{tikzpicture}
}
\caption{Preparedness Table: Das Antiperiodensystem der Elemente (Statuscodiert)}
\end{figure}
"""

os.makedirs(OUT_DIR, exist_ok=True)
with open(os.path.join(OUT_DIR, "ptable.tex"), "w", encoding="utf-8") as f:
    f.write(tex_code)
