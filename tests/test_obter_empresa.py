import pytest
from core.use_cases.obter_empresa import ObterEmpresa
from core.entities.empresa import Empresa

def test_obter_empresa(mocker):
    # Mock do repositório
    repositorio_mock = mocker.Mock()
    empresa_mock = Empresa(id="empresas-1", nome="Empresa Teste", endereco="Rua ABC", cnpj="00.000.000/0001-00", email="teste@empresa.com")
    repositorio_mock.obter.return_value = empresa_mock

    # Instancia o caso de uso
    use_case = ObterEmpresa(repositorio_mock)

    # Executa o caso de uso
    empresa = use_case.executar("empresas-1")

    # Verifica se o método obter foi chamado com os argumentos corretos
    repositorio_mock.obter.assert_called_once_with("empresas-1")

    # Verifica os valores retornados
    assert empresa.id == "empresas-1"
    assert empresa.nome == "Empresa Teste"
    assert empresa.email == "teste@empresa.com"
