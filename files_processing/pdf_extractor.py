import boto3
import re
from dtos.ExtractedDataDTO import ExtractedDataDTO

def extract_data_with_textract(pdf_file_path):
    textract = boto3.client('textract', region_name='us-east-1')

    # Chame o serviço Textract para analisar o documento PDF
    with open(pdf_file_path, 'rb') as file:
        response = textract.analyze_document(
            Document={
                'Bytes': file.read()
            },
            FeatureTypes=['FORMS']
        )

    placa_list = []
    chassi_list = []
    renavam_list = []

    placa_pattern = re.compile(r'([A-z]{3}-?[0-9][0-9A-z][0-9]{2})')
    chassi_pattern = re.compile(r'([A-HJ-NPR-Z0-9]{17})')
    renavam_pattern = re.compile(r'(0\d{9,11})')

    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            text = item['Text']

            placas = re.findall(placa_pattern, text)
            placa_list.extend(placas)

            chassis = re.findall(chassi_pattern, text)
            chassi_list.extend(chassis)

            renavam = re.findall(renavam_pattern, text)
            renavam_list.extend(renavam)

    extracted_data_list = []

    for i in range(max(len(placa_list), len(chassi_list), len(renavam_list))):
        placa = placa_list[i] if i < len(placa_list) else None
        chassi = chassi_list[i] if i < len(chassi_list) else None
        renavam = renavam_list[i] if i < len(renavam_list) else None

        extracted_data_list.append(ExtractedDataDTO(placa, chassi, renavam, nome_pasta = pdf_file_path))

    return extracted_data_list

