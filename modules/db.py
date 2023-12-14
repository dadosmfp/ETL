from dotenv import load_dotenv
import pandas as pd
import os
from sqlalchemy import create_engine
from sqlalchemy import text


class DatabaseConnection:
    def __init__(self):
        """
        Initializes the object.

        Args:
            None

        Returns:
            None
        """
        load_dotenv(r'config/cfg.env')
        self.engine = None

    def connect(self):
        """
        Connects to the database using the provided environment variables for the database credentials.
        """
        try:
            db_uri = f"mysql+mysqldb://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}?ssl_ca=config/cacert-2023-08-22.pem"
            self.engine = create_engine(db_uri, echo=False)
            print("Conexão bem-sucedida!")
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def close(self):
        """
        Closes the connection to the database engine.

        This function checks if the engine object exists and, if it does, calls the `dispose()` method to close the connection. It also prints a message indicating that the connection has been closed.

        Parameters:
            None

        Returns:
            None
        """
        if self.engine:
            self.engine.dispose()
            print("Conexão fechada.")

    def drop_table(self, table_name):
        """
        Drops the specified table from the database.

        Parameters:
            table_name (str): The name of the table to be dropped.

        Returns:
            None
        """
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
        """
        Insert data from an Excel file into a specified table in the database.

        Args:
            table_name (str): The name of the table where the data will be inserted.
            excel_file (str): The path to the Excel file containing the data.

        Returns:
            None

        Raises:
            Exception: If there is an error while inserting the data.

        Example:
            insert_data_from_excel('employees', 'data.xlsx')
        """
        try:
            # Ler dados do arquivo XLSX usando pandas
            data = pd.read_excel(excel_file)
            # Inserir dados no banco de dados usando to_sql() do pandas
            data.to_sql(name=table_name, con=self.engine, if_exists='append', index=False)
            print(f"Dados do arquivo '{excel_file}' inseridos na tabela '{table_name}'.")
        except Exception as e:
            print(f"Erro ao inserir dados do arquivo na tabela: {e}")

    def create_table(self, table_name, columns):
        """
        Creates a table in the database with the specified name and columns.

        Parameters:
            table_name (str): The name of the table to be created.
            columns (dict): A dictionary where the keys are the column names and the values are the column datatypes.

        Returns:
            None

        Raises:
            Exception: If there is an error while creating the table.
        """
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
        """
        Alter a table by adding a new column.

        Parameters:
            table_name (str): The name of the table to be altered.
            new_column_name (str): The name of the new column to be added.
            new_column_datatype (str): The datatype of the new column.

        Returns:
            None

        Raises:
            Exception: If an error occurs while altering the table.
        """
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
        """
        Drops a table from the database.

        Args:
            table_name (str): The name of the table to be dropped.

        Returns:
            None

        Raises:
            Exception: If there is an error while dropping the table.
        """
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
        """
        Drops a column from the specified table.

        Parameters:
            table_name (str): The name of the table from which to drop the column.
            column_name (str): The name of the column to drop.

        Returns:
            None

        Raises:
            Exception: If there is an error while dropping the column.
        """
        try:
            with self.engine.connect() as connection:
                # Construa a instrução SQL para dropar a coluna
                drop_column_sql = text(f"ALTER TABLE `{table_name}` DROP COLUMN `{column_name}`;")
                # Execute a instrução SQL
                connection.execute(drop_column_sql)
                print(f"Coluna '{column_name}' excluída da tabela '{table_name}'.")
        except Exception as e:
            print(f"Erro ao excluir a coluna: {e}")

    def get_data_from_table(self, table_name):
        """
        Retrieves data from the specified table in the database.

        Args:
            table_name (str): The name of the table to retrieve data from.

        Returns:
            pandas.DataFrame: A DataFrame containing the retrieved data.

        Raises:
            Exception: If there is an error while retrieving data from the table.
        """
        try:
            with self.engine.connect() as connection:
                select_sql = text(f"SELECT * FROM `{table_name}`;")
                df = pd.read_sql(select_sql, connection)
                return df
        except Exception as e:
            print(f"Erro ao recuperar os dados da tabela: {e}")
