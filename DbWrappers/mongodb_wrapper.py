from abstract_wrapper import AbstractWrapper
from typing import Any
from pymongo import MongoClient
import logging


class MongoWrapper(AbstractWrapper):

    def __init__(self, dict_credentials: dict) -> None:
        super().__init__(dict_credentials)
        self.client = MongoClient(
            f"mongodb://{self.user}:{self.password}@{self.host}:{self.port}"
            )
        self.db = self.client[self.db_name]
    

    def read(self, query: str, collection: str) -> list:
        return list(self.db[collection].find(query))
    

    def create(self, data: dict, collection: str):
        result = self.db[collection].insert_one(data)
        return f"Registro inserido com sucesso: {result.inserted_id}"
    

    def update(self, collection: str, old_data: dict, new_data: dict) -> str:
        result = self.db[collection].update_one(old_data, {"$set": new_data})
        return f"Registro atualizado com sucesso: {result.upserted_id}"


    def delete(self, collection: str, query: dict) -> str:
        self.db[collection].delete_one(query)
        return f"Record {query} has been deleted successfully!" 
    

    def close(self):
        self.client.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    credentials = {
        "db_name": "olympic_dataset",
        "user": "mongo",
        "password": "senha",
        "host": "localhost",
        "port": 27017
    }

    obj_mongo = MongoWrapper(dict_credentials=credentials)
    obj_mongo.create(
        data={"nome": "João do Pulo"},
        collection="atletas")
    logging.info(f"Criado o registro...")
    
    obj_mongo.update(
        old_data={"nome": "João do Pulo"},
        new_data={"nome": "João Carlos de Oliveira"},
        collection="atletas")
    logging.info("Registro atualizado...")

    obj_mongo.delete(
        query={"nome": "João Carlos de Oliveira"},
        collection="atletas")
    logging.info("Registro deletado...")

    obj_mongo.close()
    logging.info("Conexão encerrada")