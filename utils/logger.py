import logging

# Configuração básica do logger
logging.basicConfig(
    level=logging.INFO,  # Nível de log (você pode ajustar conforme necessário)
    format='%(asctime)s [%(levelname)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Crie um objeto de logger
logger = logging.getLogger('ETLAppLogger')

# Se você deseja redirecionar os logs para um arquivo, descomente as linhas abaixo
# handler = logging.FileHandler('etl_app.log')
# formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)