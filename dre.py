import os
import pandas as pd
from utils.logger import logger
from modules.auth0 import Authenticator
from modules.transformation import DataTransformerDre, DataTransformerVendas, DataTransformerEmissao
from modules.extraction import DataExtractorOneDrive, DataExtractorRpa
from modules.loading import DataLoadingOneDrive, UploadDb
from time import sleep

class DreMacro:
    # ------------- RECEITA DRE -------------  
    def ReceitaDre(file, access_token):
        """
        Receives a file and an access token and performs the following steps:
        
        1. Logs the start of the function using the logger.info statement.
        2. Creates an instance of the DataTransformerDre class.
        3. Pauses the execution of the function for 10 seconds using the sleep function.
        4. Initiates the data transformation by calling the GetData method of the data_transformer object with the file parameter.
        5. Transforms the received data using the TransformData method of the data_transformer object with the 'Macrofrio' parameter.
        
        Parameters:
        - file: A file object to be processed.
        - access_token: An access token for authentication.
        
        Returns:
        - receita_dre: The transformed data obtained from the data_transformer object.
        """
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
        """
        This function takes in a file and an access token as parameters.
        It initializes a logger and logs the start of the DespesaDre function.
        Then it creates an instance of the DataTransformerDre class.
        After a sleep of 10 seconds, it starts the data transformation process.
        The transformed data is stored in the variable despesa_dre.
        Finally, the transformed data is further processed using the TransformData method of the DataTransformerDre class.
        The resulting transformed data is returned by the function.
        """
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
        """
        Executes the BorderoDre function.

        Parameters:
            file (str): The file to be processed.
            access_token (str): The access token for authentication.

        Returns:
            bordero_dre: The transformed bordero_dre data.
        """
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
        """
        Generate the DRE (Demonstração do Resultado do Exercício) by merging three different DataFrames: receita_dre, despesa_dre, and bordero_dre.
        
        :param access_token: The access token required for authentication.
        :type access_token: str
        
        :return: The resulting merged DataFrame containing the DRE.
        :rtype: pandas.DataFrame
        """
        receita_dre = DreMacro.ReceitaDre('receitamacro.xls', access_token)
        despesa_dre = DreMacro.DespesaDre('despesamacro.xls', access_token)
        bordero_dre = DreMacro.BorderoDre('borderomacro.xls', access_token)
        sleep(1)
        # Concatenar os DataFrames
        resultado_dre = pd.concat([receita_dre, despesa_dre, bordero_dre], ignore_index=True)
        return resultado_dre

    def EmissaoDre(file, access_token):

        # Inclua a instrução logger.info para esta função
        logger.info(f'Iniciado Emissão DRE')
        # Crie uma instância da classe DataTransformer_DRE
        data_transformer = DataTransformerEmissao()
        sleep(10)
        # Inicia a transformação de dados
        despesa_dre = data_transformer.GetData(data_transformer, f'{file}')
        despesa_dre = data_transformer.TransformData(despesa_dre,'Macrofrio')
        return despesa_dre
    
class DreTop:
    # ------------- RECEITA DRE -------------  
    def ReceitaDre(file, access_token):
        """
        Receives a file and an access token, and performs the following steps:
        1. Logs an info message indicating the start of the Receita DRE process.
        2. Creates an instance of the DataTransformerDre class.
        3. Waits for 10 seconds.
        4. Initiates the data transformation by calling the GetData method of the data_transformer object, passing the file parameter.
        5. Transforms the returned data by calling the TransformData method of the data_transformer object, passing the receita_dre data and the 'Topfrio' parameter.
        
        Returns the transformed data.

        :param file: The file to be processed.
        :type file: str
        :param access_token: The access token.
        :type access_token: str
        :return: The transformed data.
        :rtype: object
        """
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
        """
        DespesaDre is a function that takes in a file and an access_token as parameters.
        It initializes a logger and logs the start of the Despesa DRE process.
        It then creates an instance of the DataTransformerDre class.
        After a delay of 10 seconds, it starts the data transformation process.
        The transformed data is then filtered for the 'Topfrio' category.
        Finally, the transformed and filtered data is returned.
        
        Parameters:
            file (str): The file to be processed.
            access_token (str): The access token for authentication.
        
        Returns:
            despesa_dre (Any): The transformed and filtered data.
        """
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
        """
        Generate the function comment for the given function body in a markdown code block with the correct language syntax.

        :param file: The file parameter description.
        :type file: The file parameter type.
        :param access_token: The access_token parameter description.
        :type access_token: The access_token parameter type.
        :return: The return value description.
        :rtype: The return value type.
        """
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
        """
        Generates the DreTop by combining the data from three different sources: receita_dre, despesa_dre, and bordero_dre.
        
        Parameters:
            access_token (str): The access token required to authenticate the requests.
        
        Returns:
            pandas.DataFrame: The resulting DreTop DataFrame after concatenating the data from the three sources.
        """
        receita_dre = DreTop.ReceitaDre('receitatop.xls', access_token)
        despesa_dre = DreTop.DespesaDre('despesatop.xls', access_token)
        bordero_dre = DreTop.BorderoDre('borderotop.xls', access_token)
        sleep(1)
        # Concatenate the dataframes
        resultado_dre = pd.concat([receita_dre, despesa_dre, bordero_dre], ignore_index=True)
        return resultado_dre

    def EmissaoDre(file, access_token):

        # Inclua a instrução logger.info para esta função
        logger.info(f'Iniciado Emissão DRE')
        # Crie uma instância da classe DataTransformer_DRE
        data_transformer = DataTransformerEmissao()
        sleep(10)
        # Inicia a transformação de dados
        despesa_dre = data_transformer.GetData(data_transformer, f'{file}')
        despesa_dre = data_transformer.TransformData(despesa_dre,'Topfrio')
        return despesa_dre


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
    comando = 'java -jar "sikulixide-2.0.5-win.jar" -r "emissaomacro.sikuli"'
    extrator = DataExtractorRpa(comando)
    extrator.rpa()
    comando = 'java -jar "sikulixide-2.0.5-win.jar" -r "emissaotop.sikuli"'
    extrator = DataExtractorRpa(comando)
    extrator.rpa()
    authenticator = Authenticator('config\\cfg.env')
    access_token = authenticator.authenticate()
    if access_token:
        data_loader = DataLoadingOneDrive('config\\cfg.env', access_token)
        data_extractor = DataExtractorOneDrive('config\\cfg.env', access_token)
        macrofrio = DreMacro.EmissaoDre('emissaomacro.xls',access_token)
        topfrio = DreTop.EmissaoDre('emissatop.xls' ,access_token)
        base_final = pd.concat([macrofrio, topfrio], ignore_index=True)
        base_final.to_excel('data\\baseemissao.xlsx')
        data_loader.upload_dre(
            folder_id='436041249D165BBA%216218', 
            destination_folder_id='436041249D165BBA%216217',
            old_file_name='baseemissao.xlsx',
            file_name='baseemissao.xlsx',
            file_path='data\\baseemissao.xlsx'
        )
    LimpaData("data")