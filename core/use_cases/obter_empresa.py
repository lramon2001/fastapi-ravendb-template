from core.entities.empresa import Empresa
from interfaces.repositorio_empresa import RepositorioEmpresa

class ObterEmpresa:
    def __init__(self, repositorio: RepositorioEmpresa):
        self.repositorio = repositorio

    def executar(self, empresa_id: str) -> Empresa:
        empresa = self.repositorio.obter(empresa_id)
        if not empresa:
            raise ValueError(f"Empresa com ID {empresa_id} não encontrada.")
        return empresa
