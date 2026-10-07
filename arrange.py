"""Copies the chapter PDFs from the repo root into www/pdfs/ under the names the app expects.
PDFs are matched by the two digits they start with: "01 ...pdf" -> Chapter 1 ... "19 ...pdf" -> Chapter 19.
No renaming needed."""
import glob, os, re, shutil

CHAPTERS = [  # (number, expected name)
    (1, "01-the-living-world"),
    (2, "02-biological-classification"),
    (3, "03-plant-kingdom"),
    (4, "04-animal-kingdom"),
    (5, "05-morphology-flowering-plants"),
    (6, "06-anatomy-flowering-plants"),
    (7, "07-structural-organisation-animals"),
    (8, "08-cell-unit-of-life"),
    (9, "09-biomolecules"),
    (10, "10-cell-cycle-cell-division"),
    (11, "11-photosynthesis"),
    (12, "12-respiration-in-plants"),
    (13, "13-plant-growth-development"),
    (14, "14-breathing-exchange-gases"),
    (15, "15-body-fluids-circulation"),
    (16, "16-excretory-products-elimination"),
    (17, "17-locomotion-movement"),
    (18, "18-neural-control-coordination"),
    (19, "19-chemical-coordination-integration"),
]

os.makedirs("www/pdfs", exist_ok=True)
pdfs = sorted(glob.glob("*.pdf"))
print("PDFs found in repo root:", len(pdfs))
for p in pdfs: print("  -", p)

missing = []
for n, name in CHAPTERS:
    dst = f"www/pdfs/{name}.pdf"
    exact = f"{name}.pdf"
    src = exact if exact in pdfs else None
    if not src:
        hits = [p for p in pdfs if re.match(r"\s*0*%d(?!\d)" % n, p)]
        src = hits[0] if hits else None
    if src:
        shutil.copyfile(src, dst)
        print(f"Chapter {n:02d} -> {src}")
    else:
        missing.append(n)
        print(f"::warning::Chapter {n:02d}: no matching PDF found")
if missing:
    print("Chapters without a PDF:", missing)
