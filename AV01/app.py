from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Carregar modelo
model = pickle.load(open("models/model_air_quality.pkl", "rb"))

# Ordem exata das features usadas no treinamento
FEATURE_COLUMNS = [
    "PT08.S1(CO)",
    "C6H6(GT)",
    "PT08.S2(NMHC)",
    "NOx(GT)",
    "PT08.S3(NOx)",
    "NO2(GT)",
    "PT08.S4(NO2)",
    "PT08.S5(O3)",
    "T",
    "RH",
    "AH"
]

def classificar(co):
    if co <= 4:
        return "bom"
    elif co <= 9:
        return "medio"
    else:
        return "ruim"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data:
        return jsonify({"erro": "JSON de entrada não fornecido."}), 400

    # Verificar se todas as features estão presentes
    missing = [col for col in FEATURE_COLUMNS if col not in data]
    if missing:
        return jsonify({"erro": f"Campos ausentes no JSON: {missing}"}), 400

    try:
        # Montar vetor de features na ordem correta (independente da ordem do JSON)
        values = np.array([[data[col] for col in FEATURE_COLUMNS]])

        prediction = float(model.predict(values)[0])

        return jsonify({
            "co_predito": round(prediction, 4),
            "classificacao": classificar(prediction)
        })

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
