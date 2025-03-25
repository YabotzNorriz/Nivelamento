import os
import mysql.connector
from mysql.connector import Error


def preencher_cadastro_operadoras(conexao, cursor):
    arquivo = "C:/Users/João Pedro Paes/Documents/Github/Nivelamento/resources/Relatorio_cadop - Relatorio_cadop.csv"
    if arquivo.endswith(".csv"):
        query = f"""
            LOAD DATA INFILE '{arquivo}'
            INTO TABLE cadastro_operadoras
            FIELDS TERMINATED BY ','
            OPTIONALLY ENCLOSED BY '"'
            LINES TERMINATED BY '\n'
            IGNORE 1 ROWS
            (REGISTRO_ANS,CNPJ,RAZAO_SOCIAL,NOME_FANTASIA,MODALIDADE,LOGRADOURO,
            NUMERO,COMPLEMENTO,BAIRRO, CIDADE,UF,CEP, DDD,TELEFONE,FAX,
            ENDERECO_ELETRONICO, REPRESENTANTE,CARGO_REPRESENTANTE,
            REGIAO_DE_COMERCIALIZACAO,@VAR_DATA_REGISTRO_ANS)
            SET DATA_REGISTRO_ANS =
            STR_TO_DATE(@VAR_DATA_REGISTRO_ANS, '%Y-%M-%D');
            """
        try:
            cursor.execute(query)
            print(f"Arquivo {arquivo} carregado com sucesso!")
        except Exception as e:
            print(f"Erro ao carregar o arquivo {arquivo}: {e}")


def preencher_contas_financeiras(conexao, cursor):
    pasta = "C:/Users/João Pedro Paes/Documents/Github/Nivelamento/resources/databases/"

    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".csv"):
            caminho_arquivo = os.path.join(pasta, arquivo)
            query = f"""
            LOAD DATA LOCAL INFILE "{caminho_arquivo}"
            INTO TABLE contas_financeiras
            FIELDS TERMINATED BY ';'
            ENCLOSED BY '"'
            LINES TERMINATED BY '\\n'
            IGNORE 1 ROWS
            (DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL);
            """
            try:
                cursor.execute(query)
                print(f"Arquivo {arquivo} carregado com sucesso!")
            except Exception as e:
                print(f"Erro ao carregar o arquivo {arquivo}: {e}")


try:
    conexao = mysql.connector.connect(
        host="localhost", user="root", password="100804", database="teste"
    )
    cursor = conexao.cursor()
    preencher_cadastro_operadoras(conexao, cursor)
    preencher_contas_financeiras(conexao, cursor)
except Error as e:
    print("Erro ao se conectar no servidor MySql " + e)
finally:
    conexao.close()
    cursor.close()
