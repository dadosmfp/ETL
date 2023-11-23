import os
import pandas as pd
from utils.logger import logger
from modules.auth0 import Authenticator
from modules.transformation import DataTransformerDre, DataTransformerVendas
from modules.extraction import DataExtractorOneDrive, DataExtractorRpa
from modules.loading import DataLoadingOneDrive, UploadDb
from time import sleep

class DreMacro:
    # ------------- RECEITA DRE -------------  
    def ReceitaDre(file, access_token):
        # Inclua a instrução logger.info para esta função
        logger.info(f'Iniciado Receita DRE')
        # Crie uma instância da classe DataTransformer_DRE
        data_transformer = DataTransformerDre()
        sleep(10)
        # Inicia a transformação de dados
        receita_dre = data_transformer.GetData(data_transformer, f'{file}')
        receita_dre = data_transformer.TransformData(receita_dre, 'Macrofrio')
        return receita_dre
        
    # ------------- DESPESA DRE -------------  
    def DespesaDre(file, access_token):
        # Inclua a instrução logger.info para esta função
        logger.info(f'Iniciado Despesa DRE')
        # Crie uma instância da classe DataTransformer_DRE
        data_transformer = DataTransformerDre()
        sleep(10)
        # Inicia a transformação de dados
        despesa_dre = data_transformer.GetData(data_transformer, f'{file}')
        despesa_dre = data_transformer.TransformData(despesa_dre,'Macrofrio')
        return despesa_dre

    # ------------- BORDERO DRE ------------- 
    def BorderoDre(file, access_token):
        # Inclua a instrução logger.info para esta função
        logger.info(f'Iniciado Bordero DRE')
        # Crie uma instância da classe DataTransformer_DRE
        data_transformer = DataTransformerDre()
        # Inicia a transformação de dados
        sleep(10)
        bordero_dre = data_transformer.GetData(data_transformer, f'{file}')
        bordero_dre = data_transformer.transformerBordero(bordero_dre, 'Macrofrio')
        return bordero_dre

    # ------------- BASE DRE ------------- 
    def BaseDre(access_token):
        receita_dre = DreMacro.ReceitaDre('receitamacro.xls', access_token)
        despesa_dre = DreMacro.DespesaDre('despesamacro.xls', access_token)
        bordero_dre = DreMacro.BorderoDre('borderomacro.xls', access_token)
        sleep(1)
        # Concatenar os DataFrames
        resultado_dre = pd.concat([receita_dre, despesa_dre, bordero_dre], ignore_index=True)
        return resultado_dre
    
class DreTop:
    # ------------- RECEITA DRE -------------  
    def ReceitaDre(file, access_token):
        # Inclua a instrução logger.info para esta função
        logger.info(f'Iniciado Receita DRE')
        # Crie uma instância da classe DataTransformer_DRE
        data_transformer = DataTransformerDre()
        sleep(10)
        # Inicia a transformação de dados
        receita_dre = data_transformer.GetData(data_transformer, f'{file}')
        receita_dre = data_transformer.TransformData(receita_dre, 'Topfrio')
        return receita_dre
        
    # ------------- DESPESA DRE -------------  
    def DespesaDre(file, access_token):
        # Inclua a instrução logger.info para esta função
        logger.info(f'Iniciado Despesa DRE')
        # Crie uma instância da classe DataTransformer_DRE
        data_transformer = DataTransformerDre()
        sleep(10)
        # Inicia a transformação de dados
        despesa_dre = data_transformer.GetData(data_transformer, f'{file}')
        despesa_dre = data_transformer.TransformData(despesa_dre,'Topfrio')
        return despesa_dre

    # ------------- BORDERO DRE ------------- 
    def BorderoDre(file, access_token):
        # Inclua a instrução logger.info para esta função
        logger.info(f'Iniciado Bordero DRE')
        # Crie uma instância da classe DataTransformer_DRE
        data_transformer = DataTransformerDre()
        # Inicia a transformação de dados
        sleep(10)
        bordero_dre = data_transformer.GetData(data_transformer, f'{file}')
        bordero_dre = data_transformer.transformerBordero(bordero_dre, 'Topfrio')
        return bordero_dre

    # ------------- BASE DRE ------------- 
    def BaseDre(access_token):
        receita_dre = DreTop.ReceitaDre('receitatop.xls', access_token)
        despesa_dre = DreTop.DespesaDre('despesatop.xls', access_token)
        bordero_dre = DreTop.BorderoDre('borderotop.xls', access_token)
        sleep(1)
        # Concatenar os DataFrames
        resultado_dre = pd.concat([receita_dre, despesa_dre, bordero_dre], ignore_index=True)
        return resultado_dre

class Vendas:
    def ClienteVendas(file, column_names):
        # Inclua a instrução logger.info para esta função
        #logger.info(f'Iniciado Vendas')
        # Crie uma instância da classe DataTransformer_DRE
        data_transformer = DataTransformerVendas()
        column_widths = [100] * len(column_names)
        sleep(10)
        # Inicia a transformação de dados
        df = data_transformer.GetData(data_transformer, f'{file}', column_widths, column_names)
        return df

    def PedidosVendas(file, column_names):
        # Inclua a instrução logger.info para esta função
        #logger.info(f'Iniciado Vendas')
        # Crie uma instância da classe DataTransformer_DRE
        data_transformer = DataTransformerVendas()
        column_widths = [100] * len(column_names)
        sleep(10)
        # Inicia a transformação de dados
        df = data_transformer.GetData(data_transformer, f'{file}', column_widths, column_names)
        return df

    def LtvVendas(file, column_names):
        # Inclua a instrução logger.info para esta função
        #logger.info(f'Iniciado Vendas')
        # Crie uma instância da classe DataTransformer_DRE
        data_transformer = DataTransformerVendas()
        column_widths = [100] * len(column_names)
        sleep(10)
        # Inicia a transformação de dados
        df = data_transformer.GetData(data_transformer, f'{file}', column_widths, column_names)
        return df

def LimpaData(path):
    pasta = path
    diretorio = os.listdir(pasta)
    for arquivo in diretorio:
        caminho_arquivo = os.path.join(pasta, arquivo)
        if os.path.isfile(caminho_arquivo):
            os.remove(caminho_arquivo)
        
if __name__ == "__main__":
    comando = 'java -jar "sikulixide-2.0.5-win.jar" -r "macro.sikuli"'
    extrator = DataExtractorRpa(comando)
    extrator.rpa()
    comando = 'java -jar "sikulixide-2.0.5-win.jar" -r "top.sikuli"'
    extrator = DataExtractorRpa(comando)
    extrator.rpa()
    authenticator = Authenticator('config\\cfg.env')
    access_token = authenticator.authenticate()
    if access_token:
        data_loader = DataLoadingOneDrive('config\\cfg.env', access_token)
        data_extractor = DataExtractorOneDrive('config\\cfg.env', access_token)
        macrofrio = DreMacro.BaseDre(access_token)
        topfrio = DreTop.BaseDre(access_token)
        base_final = pd.concat([macrofrio, topfrio], ignore_index=True)
        base_final.to_excel('data\\base.xlsx')
        data_loader.upload_dre(
            folder_id='436041249D165BBA%216218', 
            destination_folder_id='436041249D165BBA%216217',
            old_file_name='base.xlsx',
            file_name='base.xlsx',
            file_path='data\\base.xlsx'
        )
    LimpaData("data")
    sleep(3)
    comando = 'java -jar "sikulixide-2.0.5-win.jar" -r "comercial.sikuli"'
    extrator = DataExtractorRpa(comando)
    extrator.rpa()
    clientes = Vendas.ClienteVendas(
        'clientes.txt',
        column_names=[
            "ufcli",
            "cidadecli",
            "razsoccli",
            "id_clientes"
        ]
    )

    pedido = Vendas.PedidosVendas(
        'pedidos.txt',
        column_names=[
            'pedidoped',
            'dataped',
            'totalped',
            'tpnotaped_id',
            'codcliped_id',
            'codrepped_id',
            'empresaped'
        ]
    )

    ltv = Vendas.LtvVendas(
        'ltv.txt',
        column_names=[
            'cod_cliente',
            'cliente',
            'endereco',
            'numero',
            'ddd',
            'celular',
            'telefone',
            'email',
            'cadastro',
            'tempo_casa_anos',
            'classificacao',
            'tempo_ult_ped_meses',
            'situacao',
            'media_dias_cliente',
            'ultima_data_pedido',
            'ltv',
            'qntd_pedido'
        ]
    )
    clientes.to_excel('data\\clientes.xlsx', index=False)
    pedido.to_excel('data\\pedidos.xlsx', index=False)
    ltv.to_excel('data\\ltv.xlsx', index=False)
    db_connection = UploadDb()
    db_connection.upload_data(
        'clientes',
        'data\\clientes.xlsx'
    )
    db_connection.upload_data(
        'pedido',
        'data\\pedidos.xlsx'
    )
    db_connection.upload_data(
        'ltv',
        'data\\ltv.xlsx'
    )
    LimpaData("data")
    logger.info("Processo de ETL concluído para DRE")