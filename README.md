# 💼 Simulador Tributário - Projeto Fullstack

Este repositório contém uma aplicação completa (frontend + backend) para simular e comparar os principais regimes tributários brasileiros: **Simples Nacional**, **Lucro Presumido** e **Lucro Real**.

A ferramenta foi desenvolvida com foco em **facilidade de uso**, **velocidade de cálculo** e **educação fiscal**, ajudando micro e pequenas empresas a entenderem qual regime pode ser mais vantajoso para sua realidade.

---

## 🧩 Estrutura do Projeto

```
SIMULADOR-TRIBUTARIO/
├── backend/   → API Flask (cálculo tributário)
├── frontend/  → Aplicação Angular (interface do usuário)
```

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/AngelitaSVB/simulador-tributario.git
cd simulador-tributario
```

### 2. Execute o backend (Flask)

```bash
cd backend
python -m venv venv
venv\Scripts\activate    # Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
python app.py
```

### 3. Execute o frontend (Angular)

```bash
cd ../frontend
npm install
ng serve
```

---

## 🔍 Subprojetos com detalhes

| Diretório     | Descrição                        | Documentação       |
|---------------|----------------------------------|--------------------|
| `frontend/`   | Angular 20+ com integração HTTP  | [Leia o README →](./frontend/README.md) |
| `backend/`    | API Flask com lógica tributária  | [Leia o README →](./backend/README.md)  |

---

## ✅ Status dos Testes

![Pytest](https://img.shields.io/badge/tests-passing-brightgreen?style=flat-square)

---

## ⚠️ Observação

> ⚠️ Os cálculos fornecidos são apenas estimativas rápidas.  
> O simulador **não substitui o planejamento tributário oficial** feito por um contador.

---

## 📸 Captura de Tela

<img src="screenshot.png" alt="Captura de tela do Simulador" width="700" />

---

## 👩‍💻 Autora

Feito com 💡 por [Angelita Vilas Boas](https://github.com/AngelitaSVB)
