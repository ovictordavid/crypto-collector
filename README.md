# Crypto Collector

## Visão geral
- Script em Python que coleta dados das **20 principais** criptomoedas a partir de uma API pública (CoinGecko por padrão).
- Armazena as informações em um banco local **SQLite** (`crypto.db`).
- Permite analisar os dados no **Power BI Desktop** via conexão ODBC.

## Requisitos
- Python 3.8 ou superior
- pip atualizado
- Arquivo requirements contém bibliotecas necessárias
- Power BI Desktop 
- Driver ODBC para SQLite 

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
1. Defina as variáveis para configuração da API em `.env`.
2. Ajuste apenas a linha do caminho do banco, se necessário:
   ```dotenv
   DB_PATH=./crypto.db
   ```
3. Para usar outra API (ex:CoinCap) em vez da CoinGecko, defina em `.env`:
   ```dotenv
   API_PROVIDER=coincap
   COINCAP_API_URL=https://api.coincap.io/v2
   COINCAP_API_KEY=<sua_chave>
   ```

## Execução
```bash
python -m src.main
```
O script criará (ou atualizará conforme hora) as tabelas `cryptocurrency` e `market_data` em `crypto.db`.

## Exportação para o Power BI

### Via ODBC
1. Instale o driver ODBC SQLite e crie um DSN apontando para `crypto.db`.
2. No Power BI, escolha **Obter dados → ODBC** e selecione o DSN.
3. Carregue as tabelas `cryptocurrency` e `market_data` e crie o relacionamento necessário.

## Estrutura de diretórios
```
crypto-collector/
├── src/
│   ├── api_client.py
│   ├── config.py
│   ├── db.py
│   ├── models.py
│   └── main.py
├── requirements.txt
├── .env.example
└── README.md
```
