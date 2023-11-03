import os
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import msal

class Authenticator:
    def __init__(self, env_file_path):
        # Inicializa a classe Authenticator com o caminho do arquivo de ambiente.
        self.env_file_path = env_file_path
        self.env_vars = {}
        self.client_id = ''
        self.client_secret = ''
        self.redirect_uri = ''
        self.token_url = ''
        self.scopes = []
        self.authority = ''
        self.CHROME_PROFILE_PATH = ''

    def load_environment_variables(self):
        try:
            # Carrega as variáveis de ambiente a partir do arquivo especificado.
            with open(self.env_file_path, 'r') as env_file:
                for line in env_file:
                    key, value = line.strip().split('=', 1)
                    value = value.strip("'")
                    self.env_vars[key] = value
            # Atribui as variáveis de ambiente aos atributos da classe.
            self.client_id = self.env_vars.get('client_id', '')
            self.client_secret = self.env_vars.get('client_secret', '')
            self.redirect_uri = self.env_vars.get('redirect_uri', '')
            self.token_url = self.env_vars.get('token_url', '')
            self.scopes = [scope.strip() for scope in self.env_vars.get('scopes', '').split(',')]
            self.authority = self.env_vars.get('authority', '')
            self.CHROME_PROFILE_PATH = self.env_vars.get('chrome_profile_path', '')
        except Exception as e:
            logger.error(f"Erro ao carregar variáveis de ambiente: {e}")
            raise e

    def authenticate(self):
        try:
            # Carregue as variáveis de ambiente antes de criar o aplicativo msal.
            self.load_environment_variables()
            
            app = msal.ConfidentialClientApplication(
                self.client_id,
                authority=self.authority,
                client_credential=self.client_secret,
            )
            auth_url = app.get_authorization_request_url(self.scopes)
            
            '''   -------- WEBDRIVER --------  '''
            # Crie o serviço do ChromeDriver usando o ChromeDriverManager.
            chrome_driver_service = ChromeService(ChromeDriverManager().install())
            # Defina o caminho completo para o diretório de perfil do usuário.
            user_profile_dir = os.path.join(os.getcwd(), self.CHROME_PROFILE_PATH)
            # Crie uma instância do driver do Chrome e configure o perfil do usuário.
            options = Options()
            options.add_argument(f"--user-data-dir={user_profile_dir}")
            options.add_argument("--no-sandbox")
            driver = webdriver.Chrome(service=chrome_driver_service, options=options)
            driver.get(auth_url)

            wait = WebDriverWait(driver, 10)
            try:
                button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="appConfirmContinue"]')))
                if button.is_displayed():
                    button.click()
            except TimeoutException:
                logger.info('O botão não foi encontrado ou não está visível')
            
            current_url = driver.current_url
            driver.quit()
            
            code = current_url.split('code=')[1].split('&')[0]
            result = app.acquire_token_by_authorization_code(code, scopes=self.scopes)
            
            if 'access_token' in result:
                return result['access_token']
            else:
                raise Exception('Erro ao obter token de acesso')
        except Exception as e:
            logger.error(f"Erro na autenticação: {e}")
            raise e

    def list_files(self, access_token):
        try:
            # Lista os arquivos do OneDrive usando o token de acesso fornecido.
            onedrive_api_url = 'https://graph.microsoft.com/v1.0/me/drive/root/children'
            headers = {
                'Authorization': 'Bearer ' + access_token
            }
            response = requests.get(onedrive_api_url, headers=headers)
            logger.info(response)
            if response.status_code == 200:
                files = response.json()['value']
                for file in files:
                    logger.info(f'Nome do arquivo: {file["name"]}')
            else:
                logger.error(f'Erro ao listar os arquivos. Código de status: {response.status_code}')
        except Exception as e:
            logger.error(f"Erro ao listar os arquivos: {e}")
            raise e
        
    def download_file(self, access_token, folder_id, file_name):
        try:
            # Monta a URL para fazer o download do arquivo com base no ID da pasta e no nome do arquivo.
            download_url = f'https://graph.microsoft.com/v1.0/me/drive/items/{folder_id}:/{file_name}:/content'
            headers = {
                'Authorization': 'Bearer ' + access_token
            }
            response = requests.get(download_url, headers=headers)
            if response.status_code == 200:
                # Verifica se a pasta de destino existe, cria se necessário.
                destination_folder = 'data'
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                # Salva o arquivo baixado na pasta de destino.
                with open(os.path.join(destination_folder, file_name), 'wb') as file:
                    file.write(response.content)
                logger.info(f'Arquivo "{file_name}" baixado com sucesso.')
            else:
                logger.error(f'Erro ao baixar o arquivo. Código de status: {response.status_code}')
        except Exception as e:
            logger.error(f"Erro ao baixar o arquivo: {e}")
            raise e
        
    def upload_file(self, access_token, folder_id, file_name, file_path):
        try:
            # Define a URL de upload com base no ID da pasta.
            upload_url = f'https://graph.microsoft.com/v1.0/me/drive/items/{folder_id}:/{file_name}:/content'
            headers = {
                'Authorization': 'Bearer ' + access_token
            }           
            # Lê o conteúdo do arquivo local.
            with open(file_path, 'rb') as file:
                file_contents = file.read()
            # Envia o arquivo para o OneDrive.
            response = requests.put(upload_url, headers=headers, data=file_contents)
            if response.status_code == 201 or 200:
                logger.info(f'Arquivo "{file_name}" foi carregado com sucesso.')
            else:
                logger.info(f'Erro ao carregar o arquivo. Código de status: {response.status_code}')
        except Exception as e:
            logger.info(f"Erro ao carregar o arquivo: {e}")
            raise e
        
    def rename_file(self, access_token, folder_id, old_file_name, new_file_name):
        try:
            # Define a URL para renomear o arquivo com base no ID do item.
            rename_url = f'https://graph.microsoft.com/v1.0/me/drive/items/{folder_id}/children/{old_file_name}'
            headers = {
                'Authorization': 'Bearer ' + access_token,
                'Content-Type': 'application/json'
            }
            # Define o novo nome do arquivo no corpo da solicitação.
            request_body = {
                'name': new_file_name
            }
            # Realiza a solicitação PATCH para renomear o arquivo.
            response = requests.patch(rename_url, headers=headers, json=request_body)
            if response.status_code == 200:
                logger.info(f'Arquivo renomeado para "{new_file_name}" com sucesso.')
            else:
                logger.error(f'Erro ao renomear o arquivo. Código de status: {response.status_code}')
        except Exception as e:
            logger.error(f"Erro ao renomear o arquivo: {e}")
            raise e
    
    def get_file_id_by_name(self, access_token, folder_id, file_name):
        try:
            # Define a URL para listar os itens na pasta com base no ID da pasta.
            list_items_url = f'https://graph.microsoft.com/v1.0/me/drive/items/{folder_id}/children'
            headers = {
                'Authorization': 'Bearer ' + access_token
            }
            response = requests.get(list_items_url, headers=headers)
            if response.status_code == 200:
                items = response.json()['value']
                for item in items:
                    if item['name'] == file_name:
                        return item['id']
                # Se o arquivo não for encontrado, retorne None.
                return None
            else:
                logger.error(f'Erro ao listar os itens na pasta. Código de status: {response.status_code}')
                return None
        except Exception as e:
            logger.error(f"Erro ao obter o ID do arquivo: {e}")
            raise e
    
    def move_file(self, access_token, source_folder_id, destination_folder_id, file_name):
        try:
            # Obtém o ID do arquivo com base no nome do arquivo e no ID da pasta de origem.
            file_id = self.get_file_id_by_name(access_token, source_folder_id, file_name)
            
            if file_id:
                # Define a URL para mover o arquivo com base no ID do item.
                move_url = f'https://graph.microsoft.com/v1.0/me/drive/items/{file_id}'
                headers = {
                    'Authorization': 'Bearer ' + access_token,
                    'Content-Type': 'application/json'
                }
                # Define o ID da pasta de destino no corpo da solicitação.
                request_body = {
                    'parentReference': {
                        'id': destination_folder_id
                    }
                }
                # Realiza a solicitação PATCH para mover o arquivo.
                response = requests.patch(move_url, headers=headers, json=request_body)
                if response.status_code == 200:
                    logger.info(f'Arquivo "{file_name}" movido para a pasta de destino com sucesso.')
                else:
                    logger.error(f'Erro ao mover o arquivo. Código de status: {response.status_code}')
            else:
                logger.error(f'Arquivo não encontrado na pasta de origem.')
        except Exception as e:
            logger.error(f"Erro ao mover o arquivo: {e}")
            raise e
