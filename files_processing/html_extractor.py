import re
from lxml import etree
from dtos.ExtractedDataDTO import ExtractedDataDTO
import logging

def extract_data_from_html(html_file_path):
    placa_list = []
    chassi_list = []
    renavam_list = []

    try:
        with open(html_file_path, 'r', encoding='latin-1') as html_file:
            html_content = html_file.read()

            try:
                tree = etree.HTML(html_content)
                descricao_lote_element = tree.xpath('//*[@id="descricaoLote"]')[0]
                descricao_lote_text = descricao_lote_element.text.strip()

                placa_pattern = re.finditer(r'(?i)(placas|placa)\s*:?\s*([A-z]{3}-?[0-9][0-9A-z][0-9]{2})', descricao_lote_text)
                chassi_pattern = re.finditer(r'(?i)(chassi\s*:?\s*)([A-HJ-NPR-Z0-9]{17})', descricao_lote_text)
                renavam_pattern = re.finditer(r'(?i)(renavam\s*:?\s*)([0-9]{9,11})', descricao_lote_text)

                for match in placa_pattern:
                    placa = match.group(2)
                    placa_list.append(placa)

                for match in chassi_pattern:
                    chassi = match.group(2)
                    chassi_list.append(chassi)

                for match in renavam_pattern:
                    renavam = match.group(2)
                    renavam_list.append(renavam)

            except IndexError:
                logging.warning("Elemento com ID 'descricaoLote' não encontrado com XPath")

    except Exception as e:
        logging.warning(f"Não foi possível abrir o arquivo: {str(e)}")


    extracted_data_list = []

    for i in range(max(len(placa_list), len(chassi_list), len(renavam_list))):
        placa = placa_list[i] if i < len(placa_list) else None
        chassi = chassi_list[i] if i < len(chassi_list) else None
        renavam = renavam_list[i] if i < len(renavam_list) else None

        extracted_data_list.append(ExtractedDataDTO(placa, chassi, renavam, nome_pasta = html_file_path))

    return extracted_data_list
