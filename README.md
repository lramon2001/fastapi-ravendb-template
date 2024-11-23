# API de Gerenciamento de Empresas

Esta é uma API para gerenciar empresas utilizando **FastAPI** como framework e **RavenDB** como banco de dados. A API segue princípios de arquitetura limpa, garantindo separação de responsabilidades e facilidade de manutenção.

---

## Pré-requisitos

Antes de rodar o projeto, certifique-se de ter:

- **Python 3.10+**
- **pip** (gerenciador de pacotes do Python)
- **RavenDB** configurado e acessível
- Certificado de cliente do RavenDB no formato `.pem`

---

## Instalação

### 1. Clone o Repositório

Execute o comando para clonar o repositório e navegar até o diretório do projeto:
```bash
git clone https://github.com/lramon2001/fastapi-ravendb-template.git 
cd fastapi-ravendb-template
```
### 2. Crie e Ative o Ambiente Virtual

- **Linux/Mac**:  
```bash
  python -m venv .venv  
  source .venv/bin/activate  
```
- **Windows**:  
```shell
  python -m venv .venv  
  .venv\Scripts\activate  
```
### 3. Instale as Dependências
```bash
pip install -r requirements.txt
```
### 4. Configure o Arquivo `.env`

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

RAVENDB_URL=
RAVENDB_DATABASE=  
RAVENDB_CERTIFICATE=

---

## Uso

### 1. Rodar a API

Execute o servidor:
```bash
uvicorn app.main:app --reload
```

A API estará disponível em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 2. Documentação da API

Acesse a documentação interativa:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- **Redoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
