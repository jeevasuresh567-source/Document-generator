import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ai_core.gemini_generator import generate_document
from services.document_service import build_docx, build_pdf, build_txt

text = generate_document("NDA", "Person A, Company B",
                         "Confidentiality; No unauthorized disclosure",
                         "01 October 2026")
assert text.strip()
assert build_txt(text).startswith(b"LEGAL DOCUMENT")
assert build_docx(text, "NDA").startswith(b"PK")
assert build_pdf(text, "NDA").startswith(b"%PDF")
print("LegalEase self-test: PASS")
