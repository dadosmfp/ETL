import os
import subprocess
from datetime import datetime, timedelta
import pandas as pd
from modules.auth0 import Authenticator
from utils.logger import logger


class DataExtractor:
    def __init__(self, data_folder="data"):
        """
        Initializes an instance of the class.

        Parameters:
            data_folder (str): The folder where the data is stored. Defaults to "data".

        Returns:
            None
        """
        self.data_folder = data_folder
        self.selected_file = None  # Adicione uma variável para armazenar o nome do arquivo selecionado

    def get_files(self, extensions=(".xls", ".xlsx", ".csv", ".txt")):
        """
        Retrieves a list of files with specified extensions from the specified data folder.

        Parameters:
            extensions (tuple, optional): A tuple of file extensions to filter the files. Defaults to (".xls", ".xlsx", ".csv", ".txt").

        Returns:
            list: A list of file names with the specified extensions.

        Raises:
            FileNotFoundError: If the specified data folder does not exist or if no files with the specified extensions are found in the folder.
        """
        # Verifica se a pasta especificada existe no diretório do projeto
        if not os.path.exists(self.data_folder):
            raise FileNotFoundError(f"A pasta '{self.data_folder}' não existe no diretório do projeto.")
        # Lista todos os arquivos na pasta especificada
        files = os.listdir(self.data_folder)
        # Filtrar os arquivos com as extensões especificadas
        filtered_files = [file for file in files if file.endswith(extensions)]
        if not filtered_files:
            raise FileNotFoundError(f"Nenhum arquivo com extensões {', '.join(extensions)} encontrado na pasta '{self.data_folder}'.")
        return filtered_files

    def select_file(self, file_name):
        """
        Verifies if the selected file exists in the specified folder.

        Parameters:
            file_name (str): The name of the file to be selected.

        Raises:
            FileNotFoundError: If the specified file does not exist in the folder.

        Returns:
            None
        """
        # Verifica se o arquivo selecionado existe na pasta especificada
        available_files = self.get_files()
        if file_name not in available_files:
            raise FileNotFoundError(f"O arquivo '{file_name}' não foi encontrado na pasta '{self.data_folder}'.")
        self.selected_file = file_name  # Armazena o nome do arquivo selecionado

    def extract_data(self, column_widths=None, column_names=None):
        """
        Extracts data from a selected file based on the file extension and returns a pandas DataFrame.

        Parameters:
            column_widths (list): A list of integers representing the widths of the columns in the fixed-width file.
            column_names (list): A list of strings representing the names of the columns in the fixed-width file.

        Returns:
            pandas.DataFrame: The extracted data as a pandas DataFrame.

        Raises:
            ValueError: If no file is selected or if both column_widths and column_names are not provided.
            Exception: If an error occurs while reading the file.
        """
        if self.selected_file is None:
            raise ValueError("Nenhum arquivo foi selecionado.")
        
        file_extension = os.path.splitext(self.selected_file)[-1].lower()
        file_path = os.path.join(self.data_folder, self.selected_file)

        if file_extension == ".txt":
            # Leitura do arquivo .txt usando pandas com codificação ISO-8859-1
            try:
                if column_widths is None or column_names is None:
                    raise ValueError("Tanto column_widths quanto column_names devem ser fornecidos.")
                
                # Leia o arquivo usando read_fwf com tamanhos e nomes de colunas personalizados
                df = pd.read_fwf(file_path, widths=column_widths, header=None, names=column_names, encoding='iso-8859-1')
                
                # Remova espaços em branco nas colunas
                df = df.apply(lambda x: x.str.strip())
                
                # Definir a primeira linha como cabeçalho
                df.columns = df.iloc[0]
                
                # Remover a primeira linha (que agora é o cabeçalho)
                df = df[1:]
                
                return df
            except Exception as e:
                raise Exception(f"Erro ao ler o arquivo {file_path}: {str(e)}")
        elif file_extension in (".xls", ".xlsx", ".csv"):
            # Adicione aqui o código para lidar com outros tipos de arquivo, se necessário
            try:
                df = pd.read_excel(file_path)
                return df
            except Exception as e:
                raise Exception(f"Erro ao ler o arquivo {file_path}: {str(e)}")
        else:
            raise ValueError(f"Tipo de arquivo não suportado: {file_extension}")

class DataExtractorOneDrive:
    def __init__(self, env_file_path, access_token):
        """
        Initializes the object with the given environment file path and access token.

        :param env_file_path: The file path to the environment file.
        :type env_file_path: str
        :param access_token: The access token for authentication.
        :type access_token: str
        """
        self.authenticator = Authenticator(env_file_path)
        self.access_token = access_token

    def dre_extractor(self, folder_id, old_file_name, destination_folder_id, folder_download, file_name_download):
        """
        Extracts a file from a specified folder and renames it with the current date.
        
        Args:
            folder_id (str): The ID of the folder containing the file.
            old_file_name (str): The name of the file to be extracted and renamed.
            destination_folder_id (str): The ID of the destination folder where the renamed file will be moved to.
            folder_download (str): The folder path where the new file will be downloaded to.
            file_name_download (str): The name of the new file to be downloaded.
        
        Raises:
            Exception: If there is an error during the extraction, renaming, moving, or downloading process.
        """
        try:
            # Calcule a data para o novo nome do arquivo
            data_atual = datetime.now()
            data_anterior = data_atual - timedelta(days=1)
            data_formatada = data_anterior.strftime("%d%m%Y")  # Remova as barras para evitar caracteres inválidos
            # Remova a extensão .xlsx do nome antigo se existir
            old_file_name_without_extension = old_file_name.replace('.xlsx', '')
            new_file_name = f"{old_file_name}{data_formatada}.xlsx"  # Adicione uma extensão válida, como .xlsx
            # Renomeie a base antiga e salve na pasta de histórico
            self.authenticator.rename_file(self.access_token, folder_id, old_file_name, new_file_name)
            self.authenticator.move_file(self.access_token, folder_id, destination_folder_id, new_file_name)
            # Faça download da nova base
            self.authenticator.download_file(self.access_token, folder_download, file_name_download)
        except Exception as e:
            raise Exception(f"Erro: {str(e)}")

class DataExtractorRpa:
    def __init__(self, comando_java):
        """
        Initializes a new instance of the class.
        
        Parameters:
            comando_java (type): A description of the comando_java parameter.
        
        Returns:
            None
        """
        self.comando_java = comando_java

    def rpa(self):
        """
        Runs the RPA command.

        This method attempts to execute the Java command specified by the `comando_java` attribute. If the command is executed successfully, the function logs a success message using the `logger` object. If the command fails, the function logs an error message with the specific error returned by the `subprocess.CalledProcessError` exception.

        Parameters:
            self (object): The current instance of the class.

        Returns:
            None
        """
        # Tente executar o comando
        try:
            subprocess.run(self.comando_java, shell=True, check=True)
            logger.info("O comando Java foi executado com sucesso.")
        except subprocess.CalledProcessError as e:
            logger.error(f"O comando Java falhou com o seguinte erro: {e}")


