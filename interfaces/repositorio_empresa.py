from abc import ABC, abstractmethod
from core.entities.empresa import Empresa

class RepositorioEmpresa(ABC):
    @abstractmethod
    def criar(self, empresa: Empresa) -> str:
        pass

    @abstractmethod
    def obter(self, empresa_id: str) -> Empresa:
        pass

    @abstractmethod
    def atualizar(self, empresa_id: str, empresa: Empresa):
        pass

    @abstractmethod
    def deletar(self, empresa_id: str):
        pass
