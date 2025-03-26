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


@app.route("/api/busca", methods=["GET"])
def buscar_operadoras():
    query = request.args.get("query", "").lower()
    operadoras = carregar_operadoras()  # Carrega os registros do CSV

    resultados = [
        operadora
        for operadora in operadoras
        if any(
            query in operadora[campo].lower()
            for campo in [
                "Registro_ANS",
                "CNPJ",
                "Razao_Social",
                "Nome_Fantasia",
                "Modalidade",
                "Logradouro",
                "Numero",
                "Complemento",
                "Bairro",
                "Cidade",
                "UF",
                "CEP",
                "DDD",
                "Telefone",
                "Fax",
                "Endereco_eletronico",
                "Representante",
                "Cargo_Representante",
                "Regiao_de_Comercializacao",
                "Data_Registro_ANS",
            ]
        )
    ]

    return jsonify(resultados)


if __name__ == "__main__":
    app.run(debug=True)
