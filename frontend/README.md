# 💰 Simulador Tributário - Frontend

Este é o frontend do **Simulador Tributário**, uma aplicação desenvolvida com **Angular** para calcular e comparar automaticamente os regimes tributários mais vantajosos para micro e pequenas empresas.

A aplicação consome uma API em Flask (Python) hospedada na AWS Elastic Beanstalk.

---

## 🚀 Tecnologias Utilizadas

- Angular 17+
- TypeScript
- HTML / CSS
- Integração com API Flask (AWS)

---

## 📦 Instalação local

```bash
# Clone o repositório
git clone https://github.com/AngelitaSVB/simulador-tributario-frontend.git

# Acesse a pasta do projeto
cd simulador-tributario-frontend

# Instale as dependências
npm install

# Rode o projeto localmente
ng serve
```

O projeto será servido em `http://localhost:4200`.

---

## 📡 Integração com o Backend

O frontend se comunica com a seguinte URL de backend (já configurada no componente `simulador.component.ts`):

```
http://simulador-tributario-env.eba-kxrfbazi.us-east-1.elasticbeanstalk.com/calcular
```

Você pode alterar esse endpoint no arquivo:

```
src/app/simulador/simulador.component.ts
```

---

## 🏗️ Build para Produção

```bash
ng build
```

Os arquivos de produção serão gerados na pasta:

```
dist/simulador-tributario-frontend/browser
```

Esses arquivos devem ser enviados para o **bucket S3 público da AWS** para exibir a interface web.

---

## 🌐 Deploy (S3)

Para publicar o frontend:

1. Acesse o bucket S3 no painel AWS
2. Delete os arquivos antigos (se houver)
3. Envie os arquivos de `dist/simulador-tributario-frontend/browser`
4. Acesse a URL pública do bucket (exemplo):
   ```
   http://simulador-tributario-frontend.s3-website-us-east-1.amazonaws.com/
   ```

---

## ✨ Funcionalidades

- Preenchimento de dados tributários (receita, folha, despesas)
- Cálculo automático de tributos nos regimes:
  - Simples Nacional
  - Lucro Presumido
  - Lucro Real
- Sugestão automática do regime mais vantajoso
- Interface leve e responsiva

---

## ⚠️ Observação

> Este simulador tem como objetivo **fornecer uma estimativa rápida** da carga tributária nos diferentes regimes de tributação.

Os cálculos **não consideram todas as regras específicas de cada empresa**, como:
- Anexos específicos do Simples Nacional
- Fator R completo
- Tributos estaduais e municipais variáveis
- Benefícios fiscais, deduções específicas ou particularidades contábeis

Por isso, **não substitui uma análise contábil profissional**. Consulte seu contador para um planejamento tributário completo.

---

## 📸 Captura de Tela

<img src="../screenshot.png" alt="Captura de tela do Simulador" width="700" />

---

## 👩‍💻 Autor

Feito com 💡 por [Angelita Vilas Boas](https://github.com/AngelitaSVB)

---