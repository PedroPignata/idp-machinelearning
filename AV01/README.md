# 📊 API de Previsão de CO(GT)

## 🧠 Descrição

Este projeto implementa um modelo de Machine Learning para prever a concentração de monóxido de carbono (**CO(GT)**) com base em dados de qualidade do ar.

A aplicação disponibiliza um endpoint HTTP para realizar previsões a partir de um JSON de entrada.

---

## 📁 Estrutura do Projeto

```bash
.
├── app.py                  # API Flask
├── Dockerfile              # Configuração do container
├── docker-compose.yml      # Orquestração do container
├── requirements.txt        # Dependências do projeto
├── teste.json              # Exemplo de requisição
├── AV01.ipynb              # Notebook (EDA + treinamento)
│
└── models/
    └── model_air_quality.pkl   # Modelo treinado
```

---

## ⚙️ Como Executar

### 🔹 1. Acessar a pasta do projeto

```bash
cd AV01
```

---

### 🔹 2. Subir a aplicação com Docker

```bash
docker-compose up --build
```

Após a execução, a API estará disponível em:

```
http://localhost:5000
```

---

## 📡 Endpoint

### 🔹 POST `/predict`

Realiza a previsão da variável **CO(GT)** com base nos dados enviados.

---

## 📥 Exemplo de Requisição

```bash
curl -X POST http://localhost:5000/predict \
-H "Content-Type: application/json" \
-d @teste.json
```

---

## 📄 Formato do JSON de Entrada

```json
{
  "PT08.S1(CO)": 1360,
  "C6H6(GT)": 11.9,
  "PT08.S2(NMHC)": 1046,
  "NOx(GT)": 166,
  "PT08.S3(NOx)": 1056,
  "NO2(GT)": 113,
  "PT08.S4(NO2)": 1692,
  "PT08.S5(O3)": 1268,
  "T": 13.6,
  "RH": 48.9,
  "AH": 0.7578
}
```

---

## 📤 Exemplo de Resposta

```json
{
  "co_predito": 2.61,
  "classificacao": "bom"
}
```

---

## 🏷️ Classificação

A API retorna uma classificação baseada no valor previsto:

* **bom** → CO ≤ 4
* **medio** → 4 < CO ≤ 9
* **ruim** → CO > 9

---

## 🐳 Execução sem Docker (opcional)

Caso deseje rodar localmente:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

---
