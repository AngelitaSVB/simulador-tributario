from flask import Flask, request, jsonify
from flask_cors import CORS
from calculadora import comparar_regimes

app = Flask(__name__)
CORS(app)  # Permite requisições de qualquer origem

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.json
    resultado = comparar_regimes(
        data.get('receita_comercio', 0),
        data.get('receita_servico', 0),
        data.get('folha_pagamento', 0),
        data.get('despesas_anuais', 0)
    )
    return jsonify(resultado)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
