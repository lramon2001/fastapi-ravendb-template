from interfaces.repositorio_empresa import RepositorioEmpresa

class DeletarEmpresa:
    def __init__(self, repositorio: RepositorioEmpresa):
        self.repositorio = repositorio

    def executar(self, empresa_id: str):
        empresa = self.repositorio.obter(empresa_id)
        if not empresa:
            raise ValueError(f"Empresa com ID {empresa_id} não encontrada.")
        self.repositorio.deletar(empresa_id)
