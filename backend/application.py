from flask import Flask, request, jsonify
from flask_cors import CORS
from calculadora import comparar_regimes

application = Flask(__name__)  # nome importante: application
CORS(application)

@application.route('/calcular', methods=['POST'])
def calcular():
    data = request.json
    resultado = comparar_regimes(
        data.get('receita_comercio', 0),
        data.get('receita_servico', 0),
        data.get('folha_pagamento', 0),
        data.get('despesas_anuais', 0)
    )
    return jsonify(resultado)

# Esse bloco só é necessário para rodar localmente:
if __name__ == '__main__':
    application.run(debug=True)
