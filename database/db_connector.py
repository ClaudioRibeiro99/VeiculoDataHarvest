from dotenv import load_dotenv
import mysql.connector
import os
import logging

load_dotenv()

def get_mysql_connection():
    # Obter configurações de conexão do arquivo .env
    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")

    # Criar uma conexão com o banco de dados MySQL
    connection = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    return connection

def save_data_to_mysql(data, root):
    try:
        connection = get_mysql_connection()

        cursor = connection.cursor()

        renavam = data.renavam
        if renavam is not None:
            while len(renavam) < 11:
                renavam = "0" + renavam
        
        placa = data.placa
        if placa is not None:
            placa = data.placa.replace("-", "").replace(" ", "")

        sql = "INSERT INTO VeiculoDataHarvest.dados_enriquecimento (placa, chassi, renavam, caminho_pasta) VALUES (%s, %s, %s, %s)"
        values = (placa, data.chassi, renavam, data.nome_pasta)

        cursor.execute(sql, values)
        connection.commit()
        logging.info("Dados inseridos com sucesso!")
    except Exception as e:
        logging.critical(f"Erro ao salvar dos dados no banco: {str(e)}")
    finally:
        if connection:
            cursor.close()
            connection.close()