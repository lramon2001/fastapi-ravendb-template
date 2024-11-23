import pytest
from core.use_cases.criar_empresa import CriarEmpresa
from core.entities.empresa import Empresa

def test_criar_empresa(mocker):
    # Mock do repositório
    repositorio_mock = mocker.Mock()
    repositorio_mock.criar.return_value = "empresas-1"

    # Instancia o caso de uso
    use_case = CriarEmpresa(repositorio_mock)

    # Dados da empresa (agora compatível com o modelo atualizado)
    empresa = Empresa(
        nome="Empresa Teste",
        endereco="Rua ABC",
        cnpj="00.000.000/0001-00",
        email="teste@empresa.com"
    )

    # Executa o caso de uso
    empresa_id = use_case.executar(empresa)

    # Verifica se o método criar foi chamado com os argumentos corretos
    repositorio_mock.criar.assert_called_once_with(empresa)

    # Verifica o ID retornado
    assert empresa_id == "empresas-1"
