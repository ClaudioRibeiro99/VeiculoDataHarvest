import os
from files_processing import html_extractor, pdf_extractor
from database import db_connector
import logging

def process_pdf_and_html_files_in_directory(directory_path):

    for root, _, files in os.walk(directory_path):
        for file in files:
            try:
                if file.endswith(".pdf"):
                    pdf_file_path = os.path.join(root, file)
                    extracted_data_list = pdf_extractor.extract_data_with_textract(pdf_file_path)

                    for extracted_data in extracted_data_list:
                        db_connector.save_data_to_mysql(extracted_data, root)
                elif file.endswith(".html"):
                    html_file_path = os.path.join(root, file)

                    extracted_data_list = html_extractor.extract_data_from_html(html_file_path)

                    for extracted_data in extracted_data_list:
                        db_connector.save_data_to_mysql(extracted_data, root)
            except Exception as e:
                logging.warning(f'Erro ao processar arquivo {root}/{file}: {str(e)}')