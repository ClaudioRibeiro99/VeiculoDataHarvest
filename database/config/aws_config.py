# main.py

import aws_config  # Importa as configurações da AWS

# Use as configurações de autenticação da AWS
access_key_id = aws_config.AWS_ACCESS_KEY_ID
secret_access_key = aws_config.AWS_SECRET_ACCESS_KEY
region = aws_config.AWS_REGION

# Inicialize o cliente Textract com as configurações
import boto3
textract = boto3.client('textract', region_name=region,
                        aws_access_key_id=access_key_id,
                        aws_secret_access_key=secret_access_key)

# Agora você pode usar o objeto "textract" para chamar os serviços Textract
