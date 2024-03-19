from typing import List
from langchain_community.document_loaders import PyPDFLoader
from PyPDF2 import PdfReader
import base64
from PIL import Image


def get_pdf_data(pdfDocs):
    text = ""
    images = []
    for pdf in pdfDocs:
        pdfReader = PdfReader(pdf)
        for page in pdfReader.pages:
            text += page.extract_text()
            images.extend(page.images)
    return text, images


def get_pdf_pages(filePaths: List[str]):
    pdf_pages = []
    for pdf in filePaths:
        loader = PyPDFLoader(pdf)
        pdf_pages.extend(loader.load_and_split())
    return pdf_pages

