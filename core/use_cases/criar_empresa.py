from core.entities.empresa import Empresa
from interfaces.repositorio_empresa import RepositorioEmpresa

class CriarEmpresa:
    def __init__(self, repositorio: RepositorioEmpresa):
        self.repositorio = repositorio

    def executar(self, empresa: Empresa) -> str:
        return self.repositorio.criar(empresa)
