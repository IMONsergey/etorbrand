from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output/pdf/ETOR-brand-concepts-rework-2026-11-03.pdf"
BOARDS = [
    ROOT / "concepts/10-entry-point/v01/brand-board.png",
    ROOT / "concepts/11-project-space/v02/brand-board.png",
]
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
c = canvas.Canvas(str(OUTPUT), pagesize=(960, 540), pageCompression=1)
c.setTitle("ЕТОР. Новые варианты айдентики")
c.setAuthor("ЕТОР")
c.setSubject("Точка входа. Пространство возможностей. Концепции для обсуждения")
for p in BOARDS:
    c.drawImage(ImageReader(str(p)), 0, 0, width=960, height=540)
    c.showPage()
c.save()
print(OUTPUT)

