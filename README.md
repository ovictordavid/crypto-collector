# Crypto Collector

## Visão geral
- Script em Python que coleta dados das **top principais criptomoedas** do site Crypto Market Cap a partir de uma API pública (CoinGecko).
- Armazena as informações em um banco local **SQLite** (`crypto.db`).
- Permite analisar os dados no **Power BI** via conexão ODBC ao banco de dados criado.

## Requisitos
- Python 3.8 ou superior
- pip atualizado
- Bibliotecas necessárias listadas no requirements.txt
- Arquivo .env na origem do projeto com informações para conexão da API
- Power BI 
- Driver ODBC para SQLite (Conexão com Power BI)

## Instalação
```bash
# Clone o projeto
git clone https://github.com/<seu‑usuario>/crypto-collector.git
cd crypto-collector

# Crie e ative um ambiente virtual
python -m venv venv

# Windows PowerShell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\venv\Scripts\Activate.ps1

# Instale as dependências
pip install -r requirements.txt
```

## Configuração
1. Defina as variáveis para configuração da API e suas limitações, e do banco de dados e volume de ativos coletados em um arquivo `.env` na origem do projeto.
2. Após definir, cole no arquivo `.env` criado:
```
# Caminho do banco SQLite
DB_PATH=./crypto.db

# Número de criptomoedas que serão coletadas
LIMIT_ASSETS=50

# URL base da API
API_BASE=https://api.coingecko.com/api/v3

# Limites de retry: quantas tentativas e quantos segundos de espera no uso da API
MAX_ATTEMPTS=5
WAIT_SECONDS=2
```

## Execução
```bash
python -m src.main
```
O script criará (ou atualizará conforme hora atual) as tabelas `cryptocurrency` e `market_data` em `crypto.db`.

## Exportação para o Power BI

1. Instale o [Driver ODBC para SQLite](https://www.ch-werner.de/sqliteodbc/) e crie um DSN SQLite em *Ferramentas do Windows-> Fontes de Dados ODBC -> Adicionar* apontando para o arquivo do banco de dados `crypto.db`.
2. No Power BI, escolha **Obter dados → ODBC** e selecione o DSN.
3. Carregue as tabelas `cryptocurrency` e `market_data` e crie o relacionamento necessário.

## Estrutura de diretórios
- Foi utilizado uma arquitetura simples e modular em camadas
- Uma camada de apresentação (main.py)
- Uma camada de serviço para integração externa (api_client.py)
- Uma camada persistente (db.py)
- Um domínio para definir entidades do banco de dados
- Infraestrutura, onde variáveis e configurações são definidas (config.py e .env)

```
crypto-collector/
├── src/
│   ├── api_client.py
│   ├── config.py
│   ├── db.py
│   ├── models.py
│   └── main.py
|__ tests/
|   |__ test_db.py
├── requirements.txt
├── .env
|── README.md
|__dashboard.pbix
|__crypto.db
```
## Próximas etapas

- Integração com outras APIs
- Enriquecer com outras fontes de dados do mercado de criptomoedas
- Avaliar escalabilidade e acrescentar particionamento e clustering
