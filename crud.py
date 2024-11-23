from database import get_document_store
from models import Empresa

store = get_document_store()

def criar_empresa(empresa: Empresa) -> str:
    with store.open_session() as session:
        session.store(empresa)  # Salva o objeto no RavenDB
        session.save_changes()
        
        # Após salvar, o ID do documento é atribuído automaticamente pelo RavenDB
        empresa.id = session.advanced.get_document_id(empresa)
        session.save_changes()  # Atualiza o documento com o ID correto
        return empresa.id  # Retorna o ID do documento


def obter_empresa(store, empresa_id: str) -> Empresa:
    with store.open_session() as session:
        empresa_data = session.load(empresa_id)  # Carrega o documento pelo ID
        if not empresa_data:
            raise ValueError(f"Empresa com ID {empresa_id} não encontrada.")
        
        # Converta o _DynamicStructure em um dict com vars()
        empresa_dict = vars(empresa_data)
        
        # Converte o dict para o objeto Empresa
        empresa = Empresa(**empresa_dict)
        empresa.id = empresa_id  # Atribui o ID do documento ao objeto
        return empresa



def atualizar_empresa(store, empresa_id: str, empresa_dados: Empresa):
    with store.open_session() as session:
        # Carrega a empresa existente pelo ID
        empresa_atual = session.load(empresa_id)
        if not empresa_atual:
            raise ValueError(f"Empresa com ID {empresa_id} não encontrada.")
        
        # Atualiza os campos da empresa existente com os valores do modelo
        for key, value in empresa_dados.dict(exclude_unset=True).items():
            setattr(empresa_atual, key, value)
        
        session.save_changes()


def deletar_empresa(empresa_id: str):
    with store.open_session() as session:
        empresa = session.load(empresa_id)
        if not empresa:
            raise ValueError(f"Empresa com ID {empresa_id} não encontrada.")
        session.delete(empresa)
        session.save_changes()
