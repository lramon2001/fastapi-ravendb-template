from frameworks.database import get_document_store
from core.entities.empresa import Empresa
from interfaces.repositorio_empresa import RepositorioEmpresa

class RepositorioRavenDB(RepositorioEmpresa):
    def __init__(self):
        self.store = get_document_store()

    def criar(self, empresa: Empresa) -> str:
        with self.store.open_session() as session:
            session.store(empresa)
            session.save_changes()
            empresa.id = session.advanced.get_document_id(empresa)
            session.save_changes()
            return empresa.id

    def obter(self, empresa_id: str) -> Empresa:
        with self.store.open_session() as session:
            empresa_data = session.load(empresa_id)
            if not empresa_data:
                raise ValueError(f"Empresa com ID {empresa_id} não encontrada.")
            return Empresa(**vars(empresa_data))

    def atualizar(self, empresa_id: str, empresa: Empresa):
        with self.store.open_session() as session:
            empresa_atual = session.load(empresa_id)
            if not empresa_atual:
                raise ValueError(f"Empresa com ID {empresa_id} não encontrada.")
            for key, value in empresa.dict(exclude_unset=True).items():
                setattr(empresa_atual, key, value)
            session.save_changes()

    def deletar(self, empresa_id: str):
        with self.store.open_session() as session:
            empresa = session.load(empresa_id)
            if not empresa:
                raise ValueError(f"Empresa com ID {empresa_id} não encontrada.")
            session.delete(empresa)
            session.save_changes()

    def atualizar(self, empresa_id: str, empresa: Empresa):
        with self.store.open_session() as session:
            empresa_atual = session.load(empresa_id)
            if not empresa_atual:
                raise ValueError(f"Empresa com ID {empresa_id} não encontrada.")
            for key, value in empresa.dict(exclude_unset=True).items():
                setattr(empresa_atual, key, value)
            session.save_changes()

    def deletar(self, empresa_id: str):
        with self.store.open_session() as session:
            empresa = session.load(empresa_id)
            if not empresa:
                raise ValueError(f"Empresa com ID {empresa_id} não encontrada.")
            session.delete(empresa)
            session.save_changes()

