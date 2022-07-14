from flask import Flask
import random

app = Flask(__name__)

@app.route("/test")
def test_route():
    return {"message": f"Testing the connection. I'm thinking of a number {random.random()}"}
