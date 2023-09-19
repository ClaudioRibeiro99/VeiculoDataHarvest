import os
from dotenv import load_dotenv
from file_processor import process_pdf_and_html_files_in_directory
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.WARNING)

# Diretório onde os arquivos de log serão armazenados
log_dir = 'logs/'

# Criar um manipulador de rotação de arquivos diários com nome de arquivo com data
today = datetime.now()
log_filename = today.strftime('%Y-%m-%d.log')
file_handler = TimedRotatingFileHandler(
    os.path.join(log_dir, log_filename), when='midnight', interval=1, backupCount=7
)
file_handler.setFormatter(log_formatter)

# Adicionar o manipulador ao logger
logger.addHandler(file_handler)


load_dotenv()

if __name__ == "__main__":
    server_directory = r'\\192.168.0.221\dados_leilao\leilao'

    if os.path.exists(server_directory):
        try:
            process_pdf_and_html_files_in_directory(server_directory)
        except Exception as e:
            logging.error(f'Erro ao processar arquivos: {str(e)}')
    else:
        logging.critical(f'O caminho do servidor não está acessível: {server_directory}')