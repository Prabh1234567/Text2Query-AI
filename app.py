from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # 👈 This renders your frontend

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    
    # Example response (you can replace this with your real model)
    result = {"sql_query": f"SELECT * FROM employees WHERE condition = '{text}'"}
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
