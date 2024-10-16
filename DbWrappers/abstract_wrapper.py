from abc import ABC, abstractmethod
from typing import Any


class AbstractWrapper(ABC):

    def __init__(self, dict_credentials: dict):
        self.credentials = dict_credentials
        self.user = self.credentials["user"]
        self.password = self.credentials["password"]
        self.host = self.credentials["host"]
        self.port = self.credentials["port"]
        self.db_name = self.credentials["db_name"]


    @abstractmethod
    def read(self, query: str, *args):
        """Faz a busca com a query no banco de dados

        Args:
            query (str): Contém informação para buscar os dados esperados.
        """
        ...

    @abstractmethod
    def create(self, data: Any, *args):
        """Insere o dado no banco de dados

        Args:
            data (Any): dado que se deseja inserir no banco de dados.
        """
        ...

    @abstractmethod
    def update(self, query: str, data: Any, *args):
        """Atualiza um dado do banco de dados a partir de uma condição definida na query.

        Args:
            query (str): Define a condição de que dados serão atualizados.
            data (Any): Dado que corresponde à atualização.
        """
        ...
    

    @abstractmethod
    def delete(self, query: str, *args):
        """Deleta dados a partir da condição definida na query.

        Args:
            query (str): Define a condição na qual os dados serão excluídos.
        """
        ...
    
    @abstractmethod
    def close(self, *args):
        """Encerra a conexão com o banco
        """
        ...



if __name__ == "__main__":
    dict_credentials = {
        "username": "user",
        "password": "senha"
    }

    #classes abstratas não podem ser instanciadas diretamente, somente a partir de uma classe que a herde
    #por isso vai dar erro
    obj_wrapper = AbstractWrapper(dict_credentials=dict_credentials)
    #TypeError: Can't instantiate abstract class AbstractWrapper without an implementation for abstract methods 'close', 'create', 'delete', 'read', 'update'