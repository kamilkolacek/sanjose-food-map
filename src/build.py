"""Rebuild index.html from src/template.html, src/data.js and src/leaflet.css."""
from pathlib import Path
src = Path(__file__).parent
root = src.parent
t = (src / "template.html").read_text()
out = t.replace("/*LEAFLETCSS*/", (src / "leaflet.css").read_text()).replace("/*DATA*/", (src / "data.js").read_text())
(root / "index.html").write_text(out)
print("built index.html", len(out), "bytes")
