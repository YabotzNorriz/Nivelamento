import os
import mysql.connector
from mysql.connector import Error


def preencher_cadastro_operadoras(conexao, cursor):
    arquivo = "resources/Relatorio_cadop - Relatorio_cadop.csv"
    if arquivo.endswith(".csv"):
        query = f"""
            LOAD DATA INFILE '{arquivo}'
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


def preencher_contas_financeiras(conexao, cursor):
    pasta = "resources/anexos/"

    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".csv"):
            caminho_arquivo = os.path.join(pasta, arquivo)
            query = f"""
            LOAD DATA INFILE '{caminho_arquivo}'
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
