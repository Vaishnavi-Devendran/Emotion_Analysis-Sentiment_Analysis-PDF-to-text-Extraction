from utils import pdf_text, save_text_to_file
import os

# Define the directory paths
pdf_directory = r'/content/drive/MyDrive/HR-App/Not Shortlisted'  # Name of the directory where your PDFs are located
text_directory = r'/content/drive/MyDrive/HR-App/texts'  # Name of the directory where you want to save the text files


def extract_texts(pdf_directory, text_directory):
    # Create the text directory if it doesn't exist
    if not os.path.exists(text_directory):
        os.makedirs(text_directory)

    # Loop through each PDF in the pdf directory
    for pdf_file in os.listdir(pdf_directory):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_directory, pdf_file)
            extracted_text = pdf_text(pdf_path)

            # Define the file path for saving the text
            base_filename = os.path.splitext(pdf_file)[0]
            text_file_path = os.path.join(text_directory, f'{base_filename}.txt')

            # Save the extracted text to the file
            save_text_to_file(extracted_text, text_file_path)

            print(f"Text saved to {text_file_path}")