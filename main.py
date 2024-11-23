from fastapi import FastAPI, HTTPException
from models import Empresa
from crud import criar_empresa, obter_empresa, atualizar_empresa, deletar_empresa
from database import get_document_store

app = FastAPI()
store = get_document_store()

@app.post("/empresas/")
def criar_empresa_endpoint(empresa: Empresa):
    try:
        empresa_id = criar_empresa(empresa)
        return {"id": empresa_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/empresas/{empresa_id}")
def obter_empresa_endpoint(empresa_id: str):
    try:
        # Passe o store para a função obter_empresa
        return obter_empresa(store, empresa_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.put("/empresas/{empresa_id}")
def atualizar_empresa_endpoint(empresa_id: str, empresa: Empresa):
    try:
        atualizar_empresa(store, empresa_id, empresa)
        return {"message": "Empresa atualizada com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/empresas/{empresa_id}")
def deletar_empresa_endpoint(empresa_id: str):
    try:
        deletar_empresa(empresa_id)
        return {"message": "Empresa deletada com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
