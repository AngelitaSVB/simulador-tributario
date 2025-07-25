import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_calcular_api_sucesso(client):
    payload = {
        "receita_comercio": 100000,
        "receita_servico": 50000,
        "folha_pagamento": 30000,
        "despesas_anuais": 20000
    }
    response = client.post('/calcular', json=payload)
    assert response.status_code == 200
    json_data = response.get_json()
    assert "lucro_presumido" in json_data
    assert "lucro_real" in json_data
    assert "simples_nacional" in json_data
    assert "melhor_regime" in json_data

def test_calcular_api_entrada_vazia(client):
    response = client.post('/calcular', json={})
    assert response.status_code == 200
    json_data = response.get_json()
    assert "lucro_presumido" in json_data
    assert "lucro_real" in json_data
    assert "simples_nacional" in json_data
    assert "melhor_regime" in json_data
