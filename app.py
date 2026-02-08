from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Econiva backend is running"

@app.route("/inquiry", methods=["POST"])
def inquiry():
    data = request.form
    print("New Inquiry:", dict(data))
    return "Inquiry received successfully"

if __name__ == "__main__":
    app.run()