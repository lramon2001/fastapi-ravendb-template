from pydantic import BaseModel
from typing import Optional

class Empresa(BaseModel):
    id: Optional[str] = None  # O campo é opcional e tem valor padrão
    nome: str
    endereco: str
    cnpj: str
    email: Optional[str] = None  # Email também é opcional
