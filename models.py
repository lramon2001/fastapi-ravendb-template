from pydantic import BaseModel
from typing import Optional

class Empresa(BaseModel):
    id: Optional[str] = None  # Usado apenas para manipulação no Python
    nome: str
    endereco: str
    cnpj: str
    email: Optional[str]

    class Config:
        extra = "ignore"  # Ignora campos extras como "@metadata"
