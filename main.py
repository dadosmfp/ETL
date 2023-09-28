import os
import pandas as pd
import requests
from utils.logger import logger
from modules.auth0 import Authenticator
from modules.transformation import DataTransformerDre
from modules.extraction import DataExtractorOneDrive, DataExtractorRpa
from modules.loading import DataLoadingOneDrive
from time import sleep

class Dre:
    # ------------- RECEITA DRE -------------  
    def ReceitaDre(file, access_token):
        # Inclua a instrução logger.info para esta função
        logger.info(f'Iniciado Receita DRE')
        access_token = access_token
        # Crie uma instância da classe DataExtractorOneDrive
        data_extractor = DataExtractorOneDrive('config/cfg.env', access_token)
        # Chame o método dre_extractor na instância criada
        data_extractor.dre_extractor(
            folder_id='436041249D165BBA!6193',
            old_file_name='receita.xlsx',
            destination_folder_id='436041249D165BBA!6192',
            folder_download='436041249D165BBA!6194',
            file_name_download='receita.xls'
        )
        # Crie uma instância da classe DataTransformer_DRE
        data_transformer = DataTransformerDre()
        sleep(10)
        # Inicia a transformação de dados
        receita_dre = data_transformer.GetData(data_transformer, f'{file}')
        receita_dre = data_transformer.TransformData(receita_dre)
        return receita_dre
        
    # ------------- DESPESA DRE -------------  
    def DespesaDre(file, access_token):
        # Inclua a instrução logger.info para esta função
        logger.info(f'Iniciado Despesa DRE')
        access_token = access_token
        # Crie uma instância da classe DataExtractorOneDrive
        data_extractor = DataExtractorOneDrive('config/cfg.env', access_token)
        # Chame o método dre_extractor na instância criada
        data_extractor.dre_extractor(
            folder_id='436041249D165BBA!6198',
            old_file_name='despesa.xlsx',
            destination_folder_id='436041249D165BBA!6196',
            folder_download='436041249D165BBA!6197',
            file_name_download='despesa.xls'
        )
        # Crie uma instância da classe DataTransformer_DRE
        data_transformer = DataTransformerDre()
        sleep(10)
        # Inicia a transformação de dados
        despesa_dre = data_transformer.GetData(data_transformer, f'{file}')
        despesa_dre = data_transformer.TransformData(despesa_dre)
        return despesa_dre

    # ------------- BORDERO DRE ------------- 
    def BorderoDre(file, access_token):
        # Inclua a instrução logger.info para esta função
        logger.info(f'Iniciado Bordero DRE')
        access_token = access_token
        data_extractor.dre_extractor(
            folder_id='436041249D165BBA!6202',
            old_file_name='bordero.xlsx',
            destination_folder_id='436041249D165BBA!6200',
            folder_download='436041249D165BBA!6201',
            file_name_download='bordero.xls'
        )
        # Crie uma instância da classe DataTransformer_DRE
        data_transformer = DataTransformerDre()
        # Inicia a transformação de dados
        sleep(10)
        bordero_dre = data_transformer.GetData(data_transformer, f'{file}')
        bordero_dre = data_transformer.transformerBordero(bordero_dre)
        return bordero_dre

    # ------------- BASE DRE ------------- 
    def BaseDre(access_token):
        receita_dre = Dre.ReceitaDre('receita.xls', access_token)
        despesa_dre = Dre.DespesaDre('despesa.xls', access_token)
        bordero_dre = Dre.BorderoDre('bordero.xls', access_token)
        sleep(1)
        # Concatenar os DataFrames
        resultado_dre = pd.concat([receita_dre, despesa_dre, bordero_dre], ignore_index=True)
        return resultado_dre.to_excel('data/base.xlsx')

def LimpaData(path):
    pasta = path
    diretorio = os.listdir(pasta)
    for arquivo in diretorio:
        caminho_arquivo = os.path.join(pasta, arquivo)
        if os.path.isfile(caminho_arquivo):
            os.remove(caminho_arquivo)
        
if __name__ == "__main__":
    authenticator = Authenticator('config/cfg.env')
    access_token = authenticator.authenticate()
    if access_token:
        data_extractor = DataExtractorOneDrive('config/cfg.env', access_token)
        Dre.BaseDre(access_token)
        data_loader = DataLoadingOneDrive('config/cfg.env', access_token)
        data_loader.upload_dre(
            folder_id='436041249D165BBA!6218', 
            old_file_name='base.xlsx',
            destination_folder_id='436041249D165BBA!6217',
            file_name='base.xlsx',
            file_path='data/base.xlsx'
        )
        LimpaData("data")
        logger.info("Processo de ETL concluído para DRE")