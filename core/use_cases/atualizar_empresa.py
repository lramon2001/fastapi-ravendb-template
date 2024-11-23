from core.entities.empresa import Empresa
from interfaces.repositorio_empresa import RepositorioEmpresa

class AtualizarEmpresa:
    def __init__(self, repositorio: RepositorioEmpresa):
        self.repositorio = repositorio

    def executar(self, empresa_id: str, empresa_dados: Empresa):

        empresa_atual = self.repositorio.obter(empresa_id)
        if not empresa_atual:
            raise ValueError(f"Empresa com ID {empresa_id} não encontrada.")
        
        for key, value in empresa_dados.dict(exclude_unset=True).items():
            setattr(empresa_atual, key, value)
        
        self.repositorio.atualizar(empresa_id, empresa_atual)
