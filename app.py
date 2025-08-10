from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and features
model = pickle.load(open("loan_model.pkl", "rb"))
features = pickle.load(open("loan_features.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')
  
@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = []

        for feat in features:
            val = float(request.form.get(feat))
            input_data.append(val)

        prediction = model.predict([input_data])[0]
        result = "Loan Approved ✅" if prediction == 1 else "Loan Rejected ❌"

        return render_template("index.html", result=result)
    except Exception as e:
        return render_template("index.html", result="Error: " + str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
