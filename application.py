from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Frostlocks Github!\n V2.0"
