import os
import json
import subprocess
import requests
from datetime import datetime, timedelta
from time import sleep
import msal
import pandas as pd
from modules.auth0 import Authenticator

class DataExtractorExcel:
    def __init__(self, data_folder="data"):
        self.data_folder = data_folder
        self.selected_file = None  # Adicione uma variável para armazenar o nome do arquivo selecionado

    def get_excel_files(self):
        # Verifica se a pasta "data" existe no diretório do projeto
        if not os.path.exists(self.data_folder):
            raise FileNotFoundError(f"A pasta '{self.data_folder}' não existe no diretório do projeto.")
        # Lista todos os arquivos na pasta "data"
        files = os.listdir(self.data_folder)
        # Filtrar os arquivos com extensões .xls, .xlsx e .csv
        excel_csv_files = [file for file in files if file.endswith((".xls", ".xlsx", ".csv"))]
        if not excel_csv_files:
            raise FileNotFoundError("Nenhum arquivo .xls, .xlsx ou .csv encontrado na pasta 'data'.")
        return excel_csv_files

    def select_excel_file(self, file_name):
        # Verifica se o arquivo selecionado existe na pasta "data"
        excel_csv_files = self.get_excel_files()
        if file_name not in excel_csv_files:
            raise FileNotFoundError(f"O arquivo '{file_name}' não foi encontrado na pasta 'data'.")
        self.selected_file = file_name  # Armazena o nome do arquivo selecionado

    def extract_data_from_selected_excel(self):
        if self.selected_file is None:
            raise ValueError("Nenhum arquivo Excel foi selecionado.")
        # Caminho completo do arquivo selecionado
        xls_file_path = os.path.join(self.data_folder, self.selected_file)
        # Leitura do arquivo .xls usando pandas
        try:
            df = pd.read_excel(xls_file_path)
            return df
        except Exception as e:
            raise Exception(f"Erro ao ler o arquivo {xls_file_path}: {str(e)}")

class DataExtractorOneDrive:
    def __init__(self, env_file_path, access_token):
        self.authenticator = Authenticator(env_file_path)
        self.access_token = access_token

    def dre_extractor(self, folder_id, old_file_name, destination_folder_id, folder_download, file_name_download):
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
        self.comando_java = comando_java

    def dre_rpa(self):
        # Tente executar o comando
        try:
            subprocess.run(self.comando_java, shell=True, check=True)
            print("O comando Java foi executado com sucesso.")
        except subprocess.CalledProcessError as e:
            print(f"O comando Java falhou com o seguinte erro: {e}")


