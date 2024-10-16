from abstract_wrapper import AbstractWrapper
from typing import Any
import logging
import psycopg2


class PostgresWrapper(AbstractWrapper):

    def __init__(self, dict_credentials: dict) -> None:
        super().__init__(dict_credentials)
        self.url = f"postgres://{self.user}:{self.password}@{self.host}/{self.db_name}"
        self.connect(self.url)


    def commit(self):
        self.connection.commit()


    def connect(self, db_url: dict):
        self.connection = psycopg2.connect(db_url)
        self.cursor = self.connection.cursor()
    

    def create(self, data: dict, table_name: str):
        keys = ", ".join(data.keys())#"key1, key2"
        values = ", ".join(["%s"] * len(data))#"%s, %s"
        insert_query = f"INSERT INTO public.{table_name} ({keys}) VALUES ({values})"
        self.cursor.execute(insert_query, tuple(data.values()))
        self.commit()
        print("Valor inserido com sucesso!")


    def read(self, table_name: str) -> list:
        self.execute(f"SELECT * FROM {table_name}")
        return self.fetchall()


    def update(self, data: dict, table_name: str):
        where_clause = data.pop("condicao", None)
        
        set_clause_query = ", ".join(f"{key} = %s" for key in data.keys())
        update_query = f"UPDATE {table_name} SET {set_clause_query} WHERE {where_clause};"
        
        values = list(data.values())

        self.cursor.execute(update_query, values)
        self.commit()
        

    def delete(self, data: dict, table_name: str):
        where_clause = ' AND '.join(f"{key} = %s" for key in data.keys())
        delete_query = f"DELETE FROM {table_name} WHERE {where_clause};"
        values = list(data.values())
        self.cursor.execute(delete_query, values)
        self.commit()
        

    def close(self):
        self.connection.close()
        self.cursor.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    credentials_postgres = {
        "db_name": "olympic_dataset",
        "user": "postgres",
        "password": "senha",
        "host": "localhost",
        "port": 5432
    }

    
    obj_postgres = PostgresWrapper(dict_credentials=credentials_postgres)
    obj_postgres.create(
        data={"nome_pais": "Brasil", "sigla": "BR", "presente_nas_olimpiadas": True},
        table_name="country"
    )
    logging.info(f"Criado o registro no Postgres...")

    obj_postgres.update(data={"nome_pais": "Portugal", "sigla": "TP", "condicao": "id = 1"}, table_name="country")
    
    logging.info("Registro atualizado no postgres...")
    obj_postgres.delete(data={"nome_pais": "Brasil", "sigla": "PT"}, table_name="country")
    logging.info("Registro deletado no postgres...")
    
