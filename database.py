import uuid
from pathlib import Path
from pyravendb.store.document_store import DocumentStore

def get_document_store():
    certificate_path = Path("/mnt/c/Users/Anderson/Downloads/free.lucaovascao.client.certificate/PEM/free.lucaovascao.client.certificate.pem")
    
    # Verifique se o caminho do certificado é válido
    if not certificate_path.exists():
        raise FileNotFoundError(f"Certificado não encontrado: {certificate_path.resolve()}")

    store = DocumentStore(
        urls=["https://a.free.lucaovascao.ravendb.cloud"],  # URL do servidor
        database="teste",  # Nome do banco
        certificate=str(certificate_path)
    )
    store.certificate_pem_path = str(certificate_path)
    store.conventions.identity_parts_separator = "-"
    store.initialize()
    return store
