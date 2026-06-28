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


# ---------------- INPUT PAGE ----------------
@app.route("/predict")
def predict_page():
    return render_template("index.html")


# ---------------- PREDICTION ----------------
@app.route("/predict", methods=["POST"])
def predict():

    data = [[
        float(request.form["id"]),
        float(request.form["MonsoonIntensity"]),
        float(request.form["TopographyDrainage"]),
        float(request.form["RiverManagement"]),
        float(request.form["Deforestation"]),
        float(request.form["Urbanization"]),
        float(request.form["ClimateChange"]),
        float(request.form["DamsQuality"]),
        float(request.form["Siltation"]),
        float(request.form["AgriculturalPractices"]),
        float(request.form["Encroachments"]),
        float(request.form["IneffectiveDisasterPreparedness"]),
        float(request.form["DrainageSystems"]),
        float(request.form["CoastalVulnerability"]),
        float(request.form["Landslides"]),
        float(request.form["Watersheds"]),
        float(request.form["DeterioratingInfrastructure"]),
        float(request.form["PopulationScore"]),
        float(request.form["WetlandLoss"]),
        float(request.form["InadequatePlanning"]),
        float(request.form["PoliticalFactors"])
    ]]

    df = pd.DataFrame(data)

    scaled = scaler.transform(df)

    prediction = model.predict(scaled)[0]

    if prediction == 1:
        return redirect(url_for("chance"))

    return redirect(url_for("no_chance"))


# ---------------- RESULT PAGES ----------------
@app.route("/chance")
def chance():
    return render_template("chance.html")


@app.route("/no_chance")
def no_chance():
    return render_template("no_chance.html")


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)