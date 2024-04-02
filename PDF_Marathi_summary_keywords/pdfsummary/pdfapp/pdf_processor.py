import PyPDF2
from indicnlp.tokenize import indic_tokenize

def process_pdf(pdf_file):
    # Open the PDF file in binary mode
    with pdf_file.open('rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Initialize a variable to store text extracted from the PDF
        extracted_text = ''

        # Extract text from each page of the PDF
        for page_num in range(len(pdf_reader.pages)):
            extracted_text += pdf_reader.pages[page_num].extract_text()

        # Tokenize the extracted text using indic-nlp-library
        tokens = indic_tokenize.trivial_tokenize(extracted_text, lang='mr')  # Specify language as Marathi

        # Process the extracted tokens

        # Extract keywords (you can use your own logic here)
        keywords = set(token for token in tokens if token.isalnum())  # Using a set to store unique keywords

        # Generate summary (without repeated sentences)
        sentences = extracted_text.split('.')
        unique_sentences = []
        for sentence in sentences:
            if sentence.strip() not in unique_sentences:
                unique_sentences.append(sentence.strip())

        # Join unique sentences to form the summary
        # Generating a longer summary by including more unique sentences
        summary = '. '.join(unique_sentences[:20])  # Adjust the number of sentences as needed

        return summary, list(keywords)  # Converting set back to list for consistency










