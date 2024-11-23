import pytest
from core.use_cases.atualizar_empresa import AtualizarEmpresa
from core.entities.empresa import Empresa

def test_atualizar_empresa(mocker):
    # Mock do repositório
    repositorio_mock = mocker.Mock()
    empresa_mock = Empresa(
        id="empresas-1",
        nome="Empresa Antiga",
        endereco="Rua Velha",
        cnpj="00.000.000/0001-00",
        email="antigo@empresa.com"
    )
    repositorio_mock.obter.return_value = empresa_mock

    # Instancia o caso de uso
    use_case = AtualizarEmpresa(repositorio_mock)

    # Dados da empresa atualizados
    empresa_dados = Empresa(
        id="empresas-1",  # Incluímos o ID aqui
        nome="Empresa Nova",
        endereco="Rua Atualizada, 456",
        cnpj="11.111.111/0001-11",
        email="novo@empresa.com"
    )

    # Executa o caso de uso
    use_case.executar("empresas-1", empresa_dados)

    # Verifica se o método obter foi chamado com o ID correto
    repositorio_mock.obter.assert_called_once_with("empresas-1")

    # Verifica se o método atualizar foi chamado com os dados corretos
    repositorio_mock.atualizar.assert_called_once()
    args = repositorio_mock.atualizar.call_args[0]
    assert args[0] == "empresas-1"
    assert args[1].nome == "Empresa Nova"
    assert args[1].endereco == "Rua Atualizada, 456"
    assert args[1].cnpj == "11.111.111/0001-11"
    assert args[1].email == "novo@empresa.com"
