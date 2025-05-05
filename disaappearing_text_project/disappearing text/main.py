import PyPDF2
import pyttsx3
#convert text to speech

# path of the PDF file
path = open('C:\\Users\\91812\\Downloads', 'rb')

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfReader(path)

# creating a page object and extracting text from each page and appending to text string
text = ""
with open('C:\\Users\91812\\PycharmProjects\\disappearingText\\sample.pdf', 'rb') as pdf_file:
    read_pdf = PyPDF2.PdfReader(pdf_file)
    number_of_pages = len(read_pdf.pages)
    for page_number in range(number_of_pages):
        page = read_pdf.pages[page_number]
        page_content = page.extract_text()
        text += page_content

# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()