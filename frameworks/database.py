from pathlib import Path
from pyravendb.store.document_store import DocumentStore
from dotenv import load_dotenv
import os

load_dotenv()

def get_document_store():
    certificate_path = Path(os.getenv("RAVENDB_CERTIFICATE"))
    if not certificate_path.exists():
        raise FileNotFoundError(f"Certificado não encontrado: {certificate_path.resolve()}")

    store = DocumentStore(
        urls=[os.getenv("RAVENDB_URL")],
        database=os.getenv("RAVENDB_DATABASE"),
        certificate=str(certificate_path)
    )
    store.conventions.identity_parts_separator = "-"
    store.initialize()
    return store
