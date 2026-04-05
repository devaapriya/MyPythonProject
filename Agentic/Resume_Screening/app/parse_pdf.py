from PyPDF2 import PdfReader

def extract_pdf(file) -> str:
    print('----------- Parsing PDF -----------')

    try:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        return str(e)
