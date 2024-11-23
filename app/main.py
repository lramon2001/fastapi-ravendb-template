from fastapi import FastAPI, HTTPException
from frameworks.repositorio_ravendb import RepositorioRavenDB
from core.entities.empresa import Empresa
from core.use_cases.criar_empresa import CriarEmpresa
from core.use_cases.obter_empresa import ObterEmpresa
from core.use_cases.atualizar_empresa import AtualizarEmpresa
from core.use_cases.deletar_empresa import DeletarEmpresa
app = FastAPI()
repositorio = RepositorioRavenDB()

@app.post("/empresas/")
def criar_empresa_endpoint(empresa: Empresa):
    try:
        use_case = CriarEmpresa(repositorio)
        empresa_id = use_case.executar(empresa)
        return {"id": empresa_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/empresas/{empresa_id}")
def obter_empresa_endpoint(empresa_id: str):
    try:
        use_case = ObterEmpresa(repositorio)
        return use_case.executar(empresa_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.put("/empresas/{empresa_id}")
def atualizar_empresa_endpoint(empresa_id: str, empresa: Empresa):
    try:
        use_case = AtualizarEmpresa(repositorio)
        use_case.executar(empresa_id, empresa)
        return {"message": "Empresa atualizada com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/empresas/{empresa_id}")
def deletar_empresa_endpoint(empresa_id: str):
    try:
        use_case = DeletarEmpresa(repositorio)
        use_case.executar(empresa_id)
        return {"message": "Empresa deletada com sucesso"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
