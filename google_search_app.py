from flask import Flask, request, render_template
import requests

app = Flask(__name__)

GOOGLE_API_KEY = "AIzaSyBzCqvkHmruul_pLXOBs3j3Ny0em4wND8U"
SEARCH_ENGINE_ID = "51339012570a348f7"

@app.route("/")
def index():
    query = request.args.get("q")
    results = []

    if query:
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": GOOGLE_API_KEY,
            "cx": SEARCH_ENGINE_ID,
            "q": query
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            results = data.get("items", [])

    return render_template("index.html", query=query, results=results)

@app.route("/summary", methods=["GET"])
def summary():
    return {
        "message": "This is my custom endpoint on RunPod!",
        "status": "working"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
