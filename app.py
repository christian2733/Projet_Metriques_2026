import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# Déposez votre code à partir d'ici :
@app.route("/contact")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"  

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

@app.route('/api/precipitations/lille')
def get_lille_precipitations():
    # Coordonnées de Lille : Lat 50.6292, Lon 3.0573
    url = "https://api.open-meteo.com/v1/forecast?latitude=50.6292&longitude=3.0573&current=precipitation&timezone=Europe%2FBerlin"
    response = requests.get(url)
    data = response.json()
    
    # On extrait la valeur actuelle (en mm)
    valeur = data.get('current', {}).get('precipitation', 0)
    return jsonify({"ville": "Lille", "precipitation": valeur, "unite": "mm"})

@app.route('/atelier')
def atelier():
    return render_template('atelier.html')

if __name__ == '__main__':
    app.run(debug=True)


# Ne rien mettre après ce commentaire
    
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
