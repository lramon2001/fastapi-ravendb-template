import pytest
from core.use_cases.deletar_empresa import DeletarEmpresa

def test_deletar_empresa(mocker):
    # Mock do repositório
    repositorio_mock = mocker.Mock()
    repositorio_mock.obter.return_value = True

    # Instancia o caso de uso
    use_case = DeletarEmpresa(repositorio_mock)

    # Executa o caso de uso
    use_case.executar("empresas-1")

    # Verifica se o método obter foi chamado com o ID correto
    repositorio_mock.obter.assert_called_once_with("empresas-1")

    # Verifica se o método deletar foi chamado com o ID correto
    repositorio_mock.deletar.assert_called_once_with("empresas-1")
