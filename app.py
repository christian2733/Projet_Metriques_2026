import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# Déposez votre code à partir d'ici :
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.get("/paris")
def api_paris():
    
    url = "https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&hourly=temperature_2m"
    response = requests.get(url)
    data = response.json()

    times = data.get("hourly", {}).get("time", [])
    temps = data.get("hourly", {}).get("temperature_2m", [])

    n = min(len(times), len(temps))
    result = [
        {"datetime": times[i], "temperature_c": temps[i]}
        for i in range(n)
    ]

    return jsonify(result)

@app.route("/rapport")
def mongraphique():
    return render_template("graphique.html")

@app.route("/desing")
def mongraphique():
    return render_template("contact.html")
    
@app.get("/data-marseille")
def api_marseille():
    url = "https://api.open-meteo.com/v1/forecast?latitude=43.2965&longitude=5.3698&hourly=windspeed_10m"
    data = requests.get(url).json()
    
    times = data["hourly"]["time"]
    winds = data["hourly"]["windspeed_10m"]
    
    result = [{"dt": times[i], "wind": winds[i]} for i in range(len(times))]
    return jsonify(result)

@app.route("/atelier")
def page_atelier():
    return render_template("atelier.html")



# Ne rien mettre après ce commentaire
    
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
