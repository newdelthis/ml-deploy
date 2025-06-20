from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model/model.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    experience = np.array(data["experience"]).reshape(-1, 1)
    prediction = model.predict(experience)
    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000, debug=True)
