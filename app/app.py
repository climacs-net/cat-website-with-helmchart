#!/usr/bin/env python3
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    cat_image = response.json()[0]["url"]
    return render_template("index.html", cat_image=cat_image)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
