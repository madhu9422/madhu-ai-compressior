from io import BytesIO
from pypdf import PdfReader

def validate_pdf(raw: bytes, filename: str) -> None:
    if not filename.lower().endswith(".pdf"):
        raise ValueError("Unsupported file type. Please upload a PDF.")
    if not raw:
        raise ValueError("The uploaded file is empty.")
    try:
        reader = PdfReader(BytesIO(raw))
        if reader.is_encrypted:
            try:
                reader.decrypt("")
            except Exception as exc:
                raise ValueError("This PDF is encrypted and cannot be read without a password.") from exc
    except Exception as exc:
        raise ValueError("The file is not a readable PDF.") from exc

def extract_pdf_text(raw: bytes) -> dict:
    reader = PdfReader(BytesIO(raw))
    pages = []
    for page_num, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        if text.strip():
            pages.append(f"[Page {page_num}]\\n{text.strip()}")
    return {"text": "\\n\\n".join(pages), "pages": len(reader.pages), "pages_with_text": len(pages)}
