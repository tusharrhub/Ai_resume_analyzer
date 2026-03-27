import pdfplumber


def parse_resume(file_path=None, text=None):
    """
    Parse resume content from PDF file or text input.

    Args:
        file_path (str): Path to PDF file
        text (str): Direct text input

    Returns:
        str: Extracted text content
    """
    if file_path:
        with pdfplumber.open(file_path) as pdf:
            text_parts = []
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)
        return "\n".join(text_parts).strip()
    elif text:
        return text.strip()
    else:
        return ""
