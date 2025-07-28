from flask import Flask, jsonify, request, send_from_directory
from models import log_incident, get_all_incidents
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="./frontend")
CORS(app)

@app.route("/api/incidents", methods=["POST"])
def create_incident():
    data = request.json
    if not data.get("title") or not data.get("description"):
        return {"error": "Invalid input"}, 400
    log_incident(data["title"], data["description"])
    return {"status": "logged"}

@app.route("/api/incidents", methods=["GET"])
def list_incidents():
    return jsonify(get_all_incidents())

@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")  # ✅ fixed!

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
