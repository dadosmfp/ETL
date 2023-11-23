from dotenv import load_dotenv
import pandas as pd
import os
from sqlalchemy import create_engine
from sqlalchemy import text


class DatabaseConnection:
    def __init__(self):
        load_dotenv(r'config/cfg.env')
        self.engine = None

    def connect(self):
        try:
            db_uri = f"mysql+mysqldb://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}?ssl_ca=config/cacert-2023-08-22.pem"
            self.engine = create_engine(db_uri, echo=False)
            print("Conexão bem-sucedida!")
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def close(self):
        if self.engine:
            self.engine.dispose()
            print("Conexão fechada.")

    def drop_table(self, table_name):
        try:
            with self.engine.connect() as connection:
                # Construa a instrução SQL para dropar a tabela
                drop_table_sql = text(f"DROP TABLE IF EXISTS {table_name};")
                # Execute a instrução SQL
                connection.execute(drop_table_sql)
                print(f"Todas as linhas da tabela '{table_name}' foram excluídas.")
        except Exception as e:
            print(f"Erro ao excluir todas as linhas da tabela: {e}")

    def insert_data_from_excel(self, table_name, excel_file):
        try:
            # Ler dados do arquivo XLSX usando pandas
            data = pd.read_excel(excel_file)
            # Inserir dados no banco de dados usando to_sql() do pandas
            data.to_sql(name=table_name, con=self.engine, if_exists='append', index=False)
            print(f"Dados do arquivo '{excel_file}' inseridos na tabela '{table_name}'.")
        except Exception as e:
            print(f"Erro ao inserir dados do arquivo na tabela: {e}")

    def create_table(self, table_name, columns):
        try:
            with self.engine.connect() as connection:
                # Construa a instrução SQL para criar a tabela
                columns_str = ', '.join([f"`{col_name}` {col_datatype}" for col_name, col_datatype in columns.items()])
                create_table_sql = text(f"CREATE TABLE IF NOT EXISTS `{table_name}` ({columns_str});")
                # Execute a instrução SQL
                connection.execute(create_table_sql)
                print(f"Tabela '{table_name}' criada com sucesso.")
        except Exception as e:
            print(f"Erro ao criar a tabela: {e}")

    def alter_table(self, table_name, new_column_name, new_column_datatype):
        try:
            with self.engine.connect() as connection:
                # Construa a instrução SQL para alterar a tabela
                alter_table_sql = text(f"ALTER TABLE `{table_name}` ADD COLUMN `{new_column_name}` {new_column_datatype};")
                # Execute a instrução SQL
                connection.execute(alter_table_sql)
                print(f"Coluna '{new_column_name}' adicionada à tabela '{table_name}'.")
        except Exception as e:
            print(f"Erro ao alterar a tabela: {e}")
    
    def drop_table(self, table_name):
        try:
            with self.engine.connect() as connection:
                # Construa a instrução SQL para dropar a tabela
                drop_table_sql = text(f"DROP TABLE IF EXISTS `{table_name}`;")
                # Execute a instrução SQL
                connection.execute(drop_table_sql)
                print(f"Tabela '{table_name}' excluída com sucesso.")
        except Exception as e:
            print(f"Erro ao excluir a tabela: {e}")

    def drop_column(self, table_name, column_name):
        try:
            with self.engine.connect() as connection:
                # Construa a instrução SQL para dropar a coluna
                drop_column_sql = text(f"ALTER TABLE `{table_name}` DROP COLUMN `{column_name}`;")
                # Execute a instrução SQL
                connection.execute(drop_column_sql)
                print(f"Coluna '{column_name}' excluída da tabela '{table_name}'.")
        except Exception as e:
            print(f"Erro ao excluir a coluna: {e}")

if __name__ == "__main__":
    

    db_connection = DatabaseConnection()
    db_connection.connect()
    db_connection.alter_table(
        table_name='ltv',
        new_column_name='cliente',
        new_column_datatype='INT'
    )
    db_connection.close()