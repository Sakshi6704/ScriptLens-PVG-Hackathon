import cv2
import numpy as np
from PIL import Image
import pytesseract
import pdfplumber

# 👇 Path to your Tesseract installation (change if different)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def preprocess_image(image_file):
    """Preprocess image for better OCR accuracy."""
    image = Image.open(image_file).convert('RGB')
    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Denoise and smooth
    gray = cv2.fastNlMeansDenoising(gray, h=30)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)

    # Adaptive thresholding
    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, 11
    )

    # Enlarge for better recognition
    resized = cv2.resize(thresh, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    return resized


def extract_text_from_image(image_file, lang="eng"):
    """
    Extract text from image using Tesseract OCR.
    :param image_file: uploaded image file
    :param lang: OCR language code(s), e.g. 'eng', 'hin', 'mar', or 'eng+hin'
    """
    processed = preprocess_image(image_file)
    config = "--oem 1 --psm 6"
    text = pytesseract.image_to_string(processed, lang=lang, config=config)
    text = " ".join(text.split())
    return text


def extract_text_from_pdf(pdf_file, lang="eng"):
    """
    Extract text from a PDF (text or scanned).
    :param pdf_file: uploaded PDF file
    :param lang: OCR language code(s)
    """
    text_content = ""

    try:
        # Try normal PDF text extraction
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text() or ""
                text_content += page_text + "\n"
        if text_content.strip():
            return text_content.strip()
    except Exception as e:
        print("⚠️ pdfplumber failed, using OCR fallback:", e)

    # OCR fallback for scanned PDFs
    from pdf2image import convert_from_bytes
    pdf_bytes = pdf_file.read()
    pages = convert_from_bytes(pdf_bytes)

    for page_image in pages:
        processed = np.array(page_image)
        text = pytesseract.image_to_string(processed, lang=lang)
        text_content += text + "\n"

    return text_content.strip()