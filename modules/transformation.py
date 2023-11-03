import pandas as pd
import json
import re 
from datetime import datetime, timedelta
from modules.extraction import DataExtractor
from utils.logger import logger


# -------------- DRE --------------
class DataTransformerDre:
    def __init__(self):
        self.data_extractor = DataExtractor()  # Crie uma instância da classe DataExtractor
        
    def ClassDre(self, df):
        # Carregar o JSON com as informações para adicionar colunas
        json_file_path = 'config\\classificacao_dre.json'
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        # Adicionar as colunas ao DataFrame
        for cod_contafin, info in data.items():
            for col_name, col_value in info.items():
                df.loc[df['cod_contafin'] == cod_contafin, col_name] = col_value
        return df
        
    def GetData(self, data_transformer, file_name):
        # Inclua a instrução logger.info para esta função
        logger.info(f'Selecionando o arquivo Excel: {file_name}')
        # Selecione o arquivo Excel que deseja transformar em DataFrame
        data_transformer.data_extractor.select_file(file_name)
        # Inclua uma instrução de log para indicar a extração dos dados
        logger.info('Extraindo os dados do arquivo selecionado...')
        # Extraia os dados do arquivo selecionado
        df = data_transformer.data_extractor.extract_data()
        # Inclua uma instrução de log para indicar o término da transformação
        logger.info('Dados extraídos com sucesso.')
        return df
    
    def TransformData(self, df, empresa):
        # Inclua a instrução logger.info para esta função
        logger.info('Iniciando transformação dos dados...')
        # Mapeamento de nomes das colunas
        novo_cabecalho = {
            'Balancete Financeiro': 'Empresa',
            'Unnamed: 1': 'Duplicata',
            'Unnamed: 2': 'Código',
            'Unnamed: 3': 'excluir',
            'Unnamed: 4': 'excluir',
            'Unnamed: 5': 'excluir',
            'Unnamed: 6': 'excluir',
            'Unnamed: 7': 'excluir',
            'Unnamed: 8': 'excluir',
            'Unnamed: 9': 'excluir',
            'Unnamed: 10': 'contafin',
            'Unnamed: 11': 'excluir',
            'Unnamed: 12': 'Cliente/Fornecedor',
            'Unnamed: 13': 'excluir',
            'Unnamed: 14': 'excluir',
            'Unnamed: 15': 'central_custo',
            'Unnamed: 16': 'excluir',
            'Unnamed: 17': 'excluir',
            'Unnamed: 18': 'excluir',
            'Unnamed: 19': 'excluir',
            'Unnamed: 20': 'excluir',
            'Unnamed: 21': 'excluir',
            'Unnamed: 22': 'excluir',
            'Unnamed: 23': 'excluir',
            'Unnamed: 24': 'excluir',
            'Unnamed: 25': 'excluir',
            'Unnamed: 26': 'excluir',
            'Unnamed: 27': 'excluir',
            'Unnamed: 28': 'excluir',
            'Unnamed: 29': 'excluir',
            'Unnamed: 30': 'excluir',
            'Unnamed: 31': 'excluir',
            'Unnamed: 32': 'excluir',
            'Unnamed: 33': 'excluir',
            'Unnamed: 34': 'excluir',
            'Unnamed: 35': 'Dt. Pgto/Rec.',
            'Unnamed: 36': 'excluir',
            'Unnamed: 37': 'excluir',
            'Unnamed: 38': 'excluir',
            'Unnamed: 39': 'valor',
            'Unnamed: 40': 'excluir',
            'Unnamed: 41': 'excluir',
            'Unnamed: 42': 'excluir',
            'Unnamed: 43': 'excluir',
            'Unnamed: 44': 'Juros',
        }
        # Renomeie as colunas
        df.rename(columns=novo_cabecalho, inplace=True)
        # Exclua as colunas não necessárias
        df.drop(columns='excluir', inplace=True)
        # Substitua valores específicos por células em branco
        df['contafin'].replace('Classificação Contas', None, inplace=True)
        df['Duplicata'].replace('Duplicata', None, inplace=True)
        # Preencha as células vazias com os valores das células acima
        df['contafin'].ffill(inplace=True)
        df['central_custo'].ffill(inplace=True)
        # Filtrar apenas as linhas onde a coluna 'Duplicata' não é nula
        df = df[df['Duplicata'].notna()]
        # Use uma expressão regular para encontrar o código na coluna "contafin" e criar uma nova coluna "cod_contafin"
        df = df.copy()
        df['cod_contafin'] = df['contafin'].str.extract(r'(\d+\.\d+\.\d+\.\d+\.\d+|\d+\.\d+\.\d+\.\d+|\d+\.\d+\.\d+)')
        # Função para remover o padrão da coluna 'contafin'
        def remove_pattern(text):
            return re.sub(r'(\d+\.\d+\.\d+\.\d+\.\d+|\d+\.\d+\.\d+.\d+|\d+\.\d+\.\d+)\s(.*)', r'\2', text)
        # Aplicar a função à coluna 'contafin'
        df.loc[:, 'contafin'] = df['contafin'].apply(remove_pattern)
        # Remove os espaços em branco à esquerda na coluna 'contafin'
        df['contafin'] = df['contafin'].str.strip()
        # Reordenar as colunas
        df = df[['Duplicata', 'cod_contafin', 'contafin', 'Cliente/Fornecedor', 'central_custo','Dt. Pgto/Rec.', 'valor', 'Juros']]
        DataTransformerDre.ClassDre(self, df)
        # Filtrar as linhas onde 'Juros' não é igual a 0
        juros_df = df[df['Juros'] != '0,00']
        # Renomear a coluna 'Juros' para 'valor' em juros_df
        juros_df.rename(columns={'Juros': 'valorj'}, inplace=True)
        # Remover a coluna 'Juros' em df e a coluna 'valor' em juros_df
        df.drop(columns=['Juros'], inplace=True)
        juros_df.drop(columns=['valor'], inplace=True)
        # Renomear a coluna 'Juros' para 'valor' em juros_df
        juros_df.rename(columns={'valorj': 'valor'}, inplace=True)
        # Verifique o valor do 'cod_contafin' é despesa ou receita
        # Para DESPESA
        juros_df.loc[juros_df['cod_contafin'].str.startswith('8'), ['contafin', 'dre_resum', 'class']] = ['Juros e Multas sobre Atraso de Pagamentos', 'Despesas Financeiras', 'Despesa Fixa']
        # Para RECEITA
        juros_df.loc[juros_df['cod_contafin'].str.startswith('7'), ['contafin', 'dre_resum', 'class']] = ['Outro Valor para Contafin', 'Outro Valor para Dre_resum', 'Outra Classe']
        # Concatenar as linhas modificadas de volta ao DataFrame original
        df = pd.concat([df, juros_df], ignore_index=True)
        # Ordenar o DataFrame pelo índice para que as linhas fiquem na ordem original
        df.sort_index(inplace=True)
        # Converter os valores da coluna 'valor' para floats
        df['valor'] = df['valor'].str.replace('.', '', regex=False)
        df['valor'] = df['valor'].str.replace(',', '.', regex=False).astype(float)
        # Aplicar a função abs() para tornar os valores positivos
        df['valor'] = df['valor'].abs()
        df['emp'] = f"{empresa}"
        # Inclua uma instrução de log para indicar o término da transformação
        logger.info('Transformação dos dados concluída.')
        return df

    def transformerBordero(self, df, empresa):
        # Inclua a instrução logger.info para esta função
        logger.info('Iniciando transformação dos dados...')
        # Expressão regular para encontrar a coluna desejada
        padrao = r'Extrato da Movimentação Bancária Período .*'
        # Encontre a coluna correspondente
        coluna_correspondente = None
        for coluna in df.columns:
            if re.match(padrao, coluna):
                coluna_correspondente = coluna
                break
        if coluna_correspondente: 
            # Mapeamento de nomes das colunas
            novo_cabecalho = {
                coluna_correspondente: 'Dt. Pgto/Rec.',
                'Unnamed: 1': 'excluir',
                'Unnamed: 2': 'excluir',
                'Unnamed: 3': 'excluir',
                'Unnamed: 4': 'central_custo',
                'Unnamed: 5': 'excluir',
                'Unnamed: 6': 'excluir',
                'Unnamed: 7': 'excluir',
                'Unnamed: 8': 'excluir',
                'Unnamed: 9': 'excluir',
                'Unnamed: 10': 'excluir',
                'Unnamed: 11': 'excluir',
                'Unnamed: 12': 'excluir',
                'Unnamed: 13': 'excluir',
                'Unnamed: 14': 'Cliente/Fornecedor',
                'Unnamed: 15': 'excluir',
                'Unnamed: 16': 'excluir',
                'Unnamed: 17': 'excluir',
                'Unnamed: 18': 'excluir',
                'Unnamed: 19': 'excluir',
                'Unnamed: 20': 'excluir',
                'Unnamed: 21': 'excluir',
                'Unnamed: 22': 'excluir',
                'Unnamed: 23': 'excluir',
                'Unnamed: 24': 'excluir',
                'Unnamed: 25': 'excluir',
                'Unnamed: 26': 'excluir',
                'Unnamed: 27': 'excluir',
                'Unnamed: 28': 'excluir',
                'Unnamed: 29': 'excluir',
                'Unnamed: 30': 'excluir',
                'Unnamed: 31': 'excluir',
                'Unnamed: 32': 'valor',
                'Unnamed: 33': 'excluir',
                'Unnamed: 34': 'excluir',
                'Unnamed: 35': 'excluir',
                'Unnamed: 36': 'excluir',
                'Unnamed: 37': 'excluir',
                'Unnamed: 38': 'excluir',
                'Unnamed: 39': 'excluir',
                'Unnamed: 40': 'excluir',
                'Unnamed: 41': 'excluir',
                'Pag: 1 de 11': 'excluir'           
            }
        # Renomeie as colunas
        df.rename(columns=novo_cabecalho, inplace=True)
        # Exclua as colunas não necessárias
        df.drop(columns='excluir', inplace=True)
        # Exclua as linhas em que a coluna "Dt. Pgto/Rec." está em branco ou contém as strings especificadas
        # Expressão regular para verificar o padrão desejado
        padrao = r'Tipo de Data:Movimento Empresa: 002-MACROFRIO EQUIPAMENTOS E ISOLAMENTOS PARA REFRIGERACAO LTDA Tipo de Movimento: 109-RECEBIMENTO DUPLICATAS DESCONTADAS BRADESCO, Listar Seq. Movimento, Totalizar por Data, Conta: - -   Banco:   Agência:   Data Base:.*'
        strings_a_buscar = ["CNPJ: 07.432.074/0001-46", 
                            padrao,
                            "Data",
                            "Dt. / Hr."]
        # Use a função lambda para criar uma condição que verifica se a coluna não contém nenhuma das strings
        condicao = lambda x: not any(s in str(x) for s in strings_a_buscar)
        df = df[df['Dt. Pgto/Rec.'].apply(condicao)]
        df = df.dropna(subset=['Dt. Pgto/Rec.'], axis=0)
        # Valores para preencher as colunas
        duplicata = ''
        cod_contafin = '7.2.03'
        contafin = 'Recebimento de Antecipação de Titulos'
        nivel1 = 'Receita'
        Nivel2 = 'Receita Bruta de Vendas'
        Nivel3 = ''
        classi = 'Receita Venda'	
        dre_resum = 'Receita Bruta Operacional'
        # Atribua os valores às colunas
        df['Duplicata'] = duplicata
        df['cod_contafin'] = cod_contafin
        df['contafin'] = contafin
        df['nivel1'] = nivel1
        df['Nivel2'] = Nivel2
        df['Nivel3'] = Nivel3
        df['class'] = classi
        df['dre_resum'] = dre_resum
        df['emp'] = f"{empresa}"
        logger.info('Transformação dos dados concluída.')
        return df

# -------------- VENDAS --------------
class DataTransformerVendas:
    def __init__(self):
        self.data_extractor = DataExtractor()  # Crie uma instância da classe DataExtractor
        
    def ClassDre(self, df):
        # Carregar o JSON com as informações para adicionar colunas
        json_file_path = 'config\\classificacao_dre.json'
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        # Adicionar as colunas ao DataFrame
        for cod_contafin, info in data.items():
            for col_name, col_value in info.items():
                df.loc[df['cod_contafin'] == cod_contafin, col_name] = col_value
        return df
        
    def GetData(self, data_transformer, file_name, column_widths, column_names):
        # Inclua a instrução logger.info para esta função
        logger.info(f'Selecionando o arquivo Excel: {file_name}')
        # Selecione o arquivo Excel que deseja transformar em DataFrame
        data_transformer.data_extractor.select_file(file_name)
        # Inclua uma instrução de log para indicar a extração dos dados
        logger.info('Extraindo os dados do arquivo selecionado...')
        # Extraia os dados do arquivo selecionado
        df = data_transformer.data_extractor.extract_data(column_widths, column_names)

        # Inclua uma instrução de log para indicar o término da transformação
        logger.info('Dados extraídos com sucesso.')
        return df