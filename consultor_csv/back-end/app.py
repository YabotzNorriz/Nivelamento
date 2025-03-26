from flask import Flask, request, jsonify
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)

ARQUIVO_CSV = "./resources/Relatorio_cadop - Relatorio_cadop.csv"


def carregar_operadoras():
    operadoras = []
    with open(ARQUIVO_CSV, newline="", encoding="utf-8") as csvfile:
        leitor = csv.DictReader(csvfile)
        for row in leitor:
            operadoras.append(row)
    return operadoras


def calcular_pontos(operadora, query, pesos):
    pontos = 0
    for campo, peso in pesos.items():
        valor = operadora.get(campo, "").lower()
        if query in valor:

            ocorrencias = valor.count(query)
            pontos += peso * ocorrencias

            if valor.startswith(query):
                pontos += peso
    return pontos


@app.route("/api/busca", methods=["GET"])
def buscar_operadoras():
    query = request.args.get("query", "").lower().strip()
    if not query:
        return jsonify([])

    operadoras = carregar_operadoras()

    pesos = {
        "Nome_Fantasia": 3,
        "Razao_Social": 3,
        "Registro_ANS": 1,
        "CNPJ": 2,
        "Modalidade": 1,
        "Logradouro": 0.5,
        "Numero": 0.5,
        "Complemento": 0.5,
        "Bairro": 1,
        "Cidade": 1,
        "UF": 0.5,
        "CEP": 0.5,
        "DDD": 0.5,
        "Telefone": 1,
        "Fax": 0.5,
        "Endereco_eletronico": 1,
        "Representante": 1,
        "Cargo_Representante": 1,
        "Regiao_de_Comercializacao": 1,
        "Data_Registro_ANS": 0.5,
    }

    resultados = []
    for operadora in operadoras:
        peso = calcular_pontos(operadora, query, pesos)
        if peso > 0:
            operadora["score"] = peso
            resultados.append(operadora)

    resultados = sorted(resultados, key=lambda o: o.get("pontos", 0), reverse=True)

    return jsonify(resultados)


if __name__ == "__main__":
    app.run(debug=True)
