from abc import ABC, abstractmethod
from typing import Dict, Callable

class OpcoesMenu(ABC):
    def __init__(self, titulo: str, descricao: str):
        self.titulo = titulo
        self.descricao = descricao
    
    @abstractmethod
    def executar(self):
        # executa as funcionalidades da opção
        pass
    