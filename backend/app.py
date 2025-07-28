from flask import Flask, request, jsonify
from models import log_incident, get_all_incidents
from flask_cors import CORS

app = Flask(__name__)
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
