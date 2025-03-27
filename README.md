# Projeto de Automação de Processos e Visualização de Dados

Este projeto consiste em uma série de scripts e ferramentas que automatizam a coleta, transformação e visualização de dados. Ele inclui:

- Um web scraper para baixar PDFs de um site.
- Um transformador de dados para converter tabelas de PDFs em arquivos CSV.
- Scripts SQL para criar e carregar dados em uma base de dados MySQL.
- Um site desenvolvido em  Vue.js e Flask para pesquisar e visualizar dados com filtros.

## Índices

1. Web scrapper
2. Transformador de dados
3. Script SQL
4. Carregamento de Tabelas CSV em python/flask
5. Site em Vue.js e Flask
6. Pré-requisitos
7. Como executar os projetos

___

### Web Scrapper

O web scraper é um script que:

- Navega até um site fornecido.
- Encontra todos os links para arquivos PDF.
- Faz o download desses PDFs para uma pasta local.

#### Tecnologias Usadas

- Python 3.12.2
- Bibliotecas: `requests`, `BeautifulSoup`, `shutil`, `zipfile`

#### Como usar

1. Configura a URL no Script
2. Execute o script:
```bash
python web_scraper.py
```
3. Os projetos serão salvos na pasta onde o script se encontra

### Transformador de dados

O transformador de dados pega PDFs com tabelas e os converte em arquivos CSV.

#### Tecnologias Utilizadas

- Python 3.12.2
- Biblioteca: `pandas`, `tabula-py`

#### Como Usar
  
- Insira o PDF na pasta de entrada (resources).
- Execute o script:
```bash
python transformador_dados.py
```
- O arquivo CSV será gerado na pasta de saída.

### Scripts SQL

O arquivo SQL cria uma base de dados MySQL com as seguintes tabelas:

1. cadastro_operadoras
    - Contém dados das operadoras.

2. contas_financeiras
    - Contém dados financeiros.

Além disso, ele carrega dados diretamente de arquivos CSV.

#### Como Usar

1. Configure o MySQL.
2. Coloque os CSV na pasta do MySQL "Uploads", por padrão esse é o _path_: `C:\ProgramData\MySQL\MySQL Server 8.0\Uploads`
3. Execute o arquivo .sql no MySQL Workbench.

### Carregamento de Tabelas com Python

Um script em Python foi desenvolvido para carregar os dados nas tabelas criadas. No entanto, devido a limitações de segurança no MySQL Developer Edition, o carregamento automatizado não foi possível.

### Site para a consulta de operadoras

O site utiliza __Flask__ como backend e __Vue.js__ como frontend. Ele permite:
- Ler os dados de um arquivo CSV.
- Pesquisar e visualizar os dados utilizando filtros baseados em pesos.

#### Tecnologias Utilizadas

- Flask
- Vue.js
- Postman

#### Postman

Todos os testes de API do postman estão na pasta `colecao-postman` dentro da pasta `consultor_csv`

___

## Pré-requisitos

- Python 3.9 ou acima
- MySQL
- Node.js 18 ou acima
- Dependências descritas em `requirements.txt` (backend) e `package.json` (frontend)

## Como executar o projeto

1. Clone o repositório
2. Configure os ambientes:

    - Ambiente virtual para os arquivos em python: `python -m venv .venv`
    - Instale dependências: `pip install -r requirements.txt`

3. Configure o banco de dados MySQL.
4. Inicie o site (backend + frontend).
