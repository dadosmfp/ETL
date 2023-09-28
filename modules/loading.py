import re 
from datetime import datetime, timedelta
from modules.auth0 import Authenticator

class DataLoadingOneDrive:
    def __init__(self, env_file_path, access_token):
        self.authenticator = Authenticator(env_file_path)
        self.access_token = access_token
        
    def upload_dre(self, folder_id, old_file_name, destination_folder_id, file_name, file_path):
        try:
            # Calcule a data para o novo nome do arquivo
            data_atual = datetime.now()
            data_anterior = data_atual - timedelta(days=1)
            data_formatada = data_anterior.strftime("%d%m%Y")  # Remova as barras para evitar caracteres inválidos
            # Remova a extensão .xlsx do nome antigo se existir
            old_file_name_without_extension = old_file_name.replace('.xlsx', '')
            new_file_name = f"{old_file_name_without_extension}{data_formatada}.xlsx"  # Adicione uma extensão válida, como .xlsx
            self.authenticator.rename_file(self.access_token, folder_id, old_file_name, new_file_name)
            self.authenticator.move_file(self.access_token, folder_id, destination_folder_id, new_file_name)
            #envia para o onedrive os arquivos
            self.authenticator.upload_file(self.access_token, folder_id, file_name, file_path)
        except Exception as e:
            print(f"Erro ao carregar o arquivo: {e}")
            raise e