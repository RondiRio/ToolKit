from abc import ABC, abstractmethod

class OpcoesMenu(ABC):
    def __init__(self, titulo: str, descricao: str = ""):
        self.titulo = titulo
        self.descricao = descricao if descricao else titulo
    
    @abstractmethod
    def executar(self):
        """Executa as funcionalidades da opção"""
        pass
    
    def __str__(self):
        return f"{self.titulo}: {self.descricao}"