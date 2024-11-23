from pathlib import Path
from pyravendb.store.document_store import DocumentStore

def get_document_store():
    certificate_path = Path("/mnt/c/Users/Anderson/Downloads/free.lucaovascao.client.certificate/PEM/free.lucaovascao.client.certificate.pem")
    if not certificate_path.exists():
        raise FileNotFoundError(f"Certificado não encontrado: {certificate_path.resolve()}")

    store = DocumentStore(
        urls=["https://a.free.lucaovascao.ravendb.cloud"],
        database="teste",
        certificate=str(certificate_path)
    )
    store.conventions.identity_parts_separator = "-"
    store.initialize()
    return store
