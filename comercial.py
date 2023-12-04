import os
import pandas as pd
from utils.logger import logger
from modules.auth0 import Authenticator
from modules.transformation import DataTransformerDre, DataTransformerVendas, DataTransformerEmissao
from modules.extraction import DataExtractorOneDrive, DataExtractorRpa
from modules.loading import DataLoadingOneDrive, UploadDb
from time import sleep

class Vendas:
    def ClienteVendas(file, column_names):
        """
        ClienteVendas is a function that takes in a file and a list of column names as parameters.
        It creates an instance of the DataTransformerVendas class and initializes the column widths to 100.
        The function then sleeps for 10 seconds before starting the data transformation.
        The GetData method of the data_transformer object is called with the file, column widths, and column names as arguments,
        and the resulting dataframe is returned.

        Parameters:
        - file (str): The path to the file to be processed.
        - column_names (list): A list of column names.

        Returns:
        - df (pandas.DataFrame): The transformed dataframe.
        """
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
        """
        Generate the function comment for the following function.

        Args:
            file (str): The file path.
            column_names (list): A list of column names.

        Returns:
            DataFrame: The transformed data.
        """
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
        """
        A function that takes a file and column names as inputs and returns a transformed dataframe.

        Parameters:
        - file (str): The path to the file to be processed.
        - column_names (list): A list of column names for the dataframe.

        Returns:
        - df (pandas.DataFrame): The transformed dataframe.
        """
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
    """
    Removes all files in the specified directory.

    Parameters:
    - path (str): The path to the directory.

    Returns:
    None
    """
    pasta = path
    diretorio = os.listdir(pasta)
    for arquivo in diretorio:
        caminho_arquivo = os.path.join(pasta, arquivo)
        if os.path.isfile(caminho_arquivo):
            os.remove(caminho_arquivo)
        
if __name__ == "__main__":
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
    comando = 'java -jar "sikulixide-2.0.5-win.jar" -r "comercial.sikuli"'
    extrator = DataExtractorRpa(comando)
    extrator.rpa()