from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Lista de cadastros de operadoras
operadoras = [
    {"nome": "Operadora A", "servico": "Internet"},
    {"nome": "Operadora B", "servico": "TV"},
    {"nome": "Operadora C", "servico": "Celular"},
    {"nome": "Super Operadora", "servico": "TV e Internet"},
]


@app.route("/api/busca", methods=["GET"])
def buscar_operadoras():
    query = request.args.get("query", "").lower()
    resultados = [
        operadora for operadora in operadoras if query in operadora["nome"].lower()
    ]
    return jsonify(resultados)


if __name__ == "__main__":
    app.run(debug=True)
