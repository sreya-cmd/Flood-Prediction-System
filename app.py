from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import joblib

# Initialize Flask App
app = Flask(__name__)

# Load Model and Scaler
model = joblib.load("models/floods.save")
scaler = joblib.load("models/transform.save")


# ---------------- HOME PAGE ----------------
@app.route("/")
def home():
    return render_template("home.html")


# ---------------- PREDICT PAGE ----------------
@app.route("/predict")
def predict_page():
    return render_template("index.html")


# ---------------- PREDICTION ----------------
@app.route("/predict", methods=["POST"])
def predict():

    data = [[
        float(request.form["MonsoonIntensity"]),
        float(request.form["TopographyDrainage"]),
        float(request.form["RiverManagement"]),
        float(request.form["ClimateChange"]),
        float(request.form["DrainageSystems"])
    ]]

    df = pd.DataFrame(
        data,
        columns=[
            "MonsoonIntensity",
            "TopographyDrainage",
            "RiverManagement",
            "ClimateChange",
            "DrainageSystems"
        ]
    )

    scaled = scaler.transform(df)

    prediction = model.predict(scaled)[0]

    print("Predicted Flood Probability:", prediction)

    if prediction >= 0.5:
        return redirect(url_for("chance"))
    else:
        return redirect(url_for("no_chance"))


# ---------------- RESULT PAGES ----------------
@app.route("/chance")
def chance():
    return render_template("chance.html")


@app.route("/no_chance")
def no_chance():
    return render_template("no_chance.html")


# ---------------- HISTORY PAGE ----------------
@app.route("/history")
def history():
    return render_template("history.html")


# ---------------- RUN APPLICATION ----------------
if __name__ == "__main__":
    app.run(debug=True)