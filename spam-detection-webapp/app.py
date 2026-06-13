from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", prediction="")

@app.route("/predict", methods=["POST"])
def predict():
    email = request.form["email"]

    data = vectorizer.transform([email])
    result = model.predict(data)[0]

    output = "🚨 Phishing Email" if result == 1 else "✅ Safe Email"

    return render_template("index.html", prediction=output)

if __name__ == "__main__":
    app.run(debug=False)   # IMPORTANT FIX