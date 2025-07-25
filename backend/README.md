# 🧮 Simulador Tributário - Backend

Este é o backend do **Simulador Tributário**, uma API desenvolvida com **Flask** que realiza cálculos estimados de tributação para micro e pequenas empresas.

> ⚠️ Esta simulação é uma estimativa e **não substitui uma consultoria contábil profissional**.

![Pytest](https://img.shields.io/badge/tests-passing-brightgreen?style=flat-square)

---

## 🚀 Tecnologias Utilizadas

- Python 3.13+
- Flask
- Flask-CORS
- Pandas, Matplotlib, FPDF
- Pytest (para testes)

---

## 📦 Estrutura

```
backend/
├── app.py                  # API Flask principal
├── calculadora.py          # Função de cálculo tributário
├── tests/
│   ├── test_calculadora.py # Testes da lógica de cálculo
│   └── test_api.py         # Testes da API Flask
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação do backend
```

---

## ▶️ Como Executar

```bash
# Instale as dependências
pip install -r requirements.txt

# Execute o servidor localmente
python app.py
```

A API estará disponível em:  
`http://localhost:5000/calcular`

---

## 🧪 Testes Automatizados

O projeto possui testes unitários e de integração criados com `pytest`:

- **Testes da lógica tributária** (`calculadora.py`)
- **Testes da API** (`/calcular`) com Flask test client
- **Testes com entradas inválidas e casos extremos**

### 🔧 Como rodar os testes

```bash
# Execute todos os testes
pytest
```

---

## 🧠 Observações

Os cálculos foram simplificados para facilitar a comparação e decisão entre regimes tributários. Não incluem todas as particularidades contábeis e fiscais aplicáveis.

---

## 📸 Captura de Tela

<img src="../screenshot.png" alt="Captura de tela do Simulador" width="700" />

---

## ✨ Feito com 💡 por [Angelita Vilas Boas](https://github.com/AngelitaSVB)
