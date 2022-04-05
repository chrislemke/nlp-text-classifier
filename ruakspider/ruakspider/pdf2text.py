from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBox
from pdfminer.layout import LTTextLine

from io import StringIO
import cleaner
import os

PDF_PATH = os.path.abspath(__file__ + f"/../../loaded/pdf")

STORE_PATH = os.path.abspath(__file__ + f"/../../output")


def philo_at_pdf2text(path):
    fp = open(path, "rb")
    parser = PDFParser(fp)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    text = ""
    print(f"Formatting: {path}")
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)
        layout = device.get_result()
        for lt_obj in layout:
            if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                text += lt_obj.get_text()
    return text


for file in os.listdir(PDF_PATH):
    if file == ".DS_Store":
        continue
    filename = file.replace(".pdf", "")
    text = philo_at_pdf2text(f"{PDF_PATH}/{filename}.pdf")
    with open(f"{STORE_PATH}/{filename}.txt", "w", encoding="UTF-8") as outfile:
        text = cleaner.philo_at_clean_up(text)
        try:
            outfile.write(text)
            print(f"Formatting finished: {filename}.pdf")
        except:
            print(f"Error writing file: {filename}")
    outfile.close()
