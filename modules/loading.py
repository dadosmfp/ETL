from datetime import datetime, timedelta
from modules.auth0 import Authenticator
from modules.db import DatabaseConnection
from utils.logger import logger

class DataLoadingOneDrive:
    def __init__(self, env_file_path, access_token):
        """
        Initializes a new instance of the class.

        Args:
            env_file_path (str): The path to the environment file.
            access_token (str): The access token.

        Returns:
            None
        """
        self.authenticator = Authenticator(env_file_path)
        self.access_token = access_token
        
    def upload_dre(self, folder_id, old_file_name, destination_folder_id, file_name, file_path):
        """
        Uploads a file to a specified destination folder in OneDrive.

        Parameters:
            folder_id (str): The ID of the folder where the file is located.
            old_file_name (str): The name of the file to be renamed.
            destination_folder_id (str): The ID of the destination folder where the file will be moved.
            file_name (str): The name of the file to be uploaded.
            file_path (str): The path to the file to be uploaded.

        Raises:
            Exception: If there is an error while uploading the file.

        Returns:
            None
        """
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
            logger.error(f"Erro ao carregar o arquivo: {e}")
            raise e
        
    def upload_vendas(self, folder_id, old_file_name, destination_folder_id, file_name, file_path):
        """
        Uploads a file to the specified destination folder in OneDrive.

        Args:
            folder_id (str): The ID of the folder where the file is currently located.
            old_file_name (str): The name of the file to be uploaded.
            destination_folder_id (str): The ID of the folder where the file should be moved.
            file_name (str): The name of the file after it has been moved to the destination folder.
            file_path (str): The local path of the file to be uploaded.

        Raises:
            Exception: If there is an error during the file upload process.

        Returns:
            None
        """
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
            logger.error(f"Erro ao carregar o arquivo: {e}")
            raise e

class UploadDb:
    def __init__(self):
        """
        Initializes an instance of the class.

        Parameters:
            None

        Returns:
            None
        """
        self.db_connection = DatabaseConnection()  # Cria uma instância da classe DatabaseConnection

    def upload_data(self, table_name, excel_file):
        """
        Uploads data to the database table.

        Args:
            table_name (str): The name of the table to upload the data to.
            excel_file (str): The path to the Excel file containing the data.

        Returns:
            None
        """
        self.db_connection.connect()  # Conecta ao banco de dados
        self.db_connection.drop_table(table_name)  # Exclui todas as linhas da tabela
        self.db_connection.insert_data_from_excel(table_name, excel_file)  # Insere dados do arquivo XLSX na tabela
        self.db_connection.close()  # Fecha a conexão com o banco de dados
