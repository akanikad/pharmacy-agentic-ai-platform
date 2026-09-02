from pathlib import Path
import re

DATA = Path(__file__).resolve().parents[2] / "data"

def _chunks(text: str, size: int = 500, overlap: int = 80):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = min(len(words), start + size)
        chunks.append(" ".join(words[start:end]))
        if end == len(words):
            break
        start = end - overlap
    return chunks

def _load():
    docs = []
    for path in DATA.rglob("*.txt"):
        text = path.read_text(encoding="utf-8")
        for i, chunk in enumerate(_chunks(text)):
            docs.append({
                "id": f"{path.stem}-{i}",
                "source": str(path.relative_to(DATA)),
                "text": chunk,
            })
    return docs

def retrieve(query: str, top_k: int = 5):
    docs = _load()
    q = set(re.findall(r"\w+", query.lower()))
    scored = []
    for d in docs:
        tokens = set(re.findall(r"\w+", d["text"].lower()))
        score = len(q & tokens) / max(len(q), 1)
        scored.append((score, d))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [d for score, d in scored[:top_k] if score > 0]
