from flask import Flask, request, jsonify
from flask_cors import CORS
import json, os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMPS_FILE = os.path.join(BASE_DIR, "camps.json")
VICTIMS_FILE = os.path.join(BASE_DIR, "victims.json")

# ---------- INIT FILES ----------
def init_files():
    if not os.path.exists(CAMPS_FILE):
        with open(CAMPS_FILE, "w") as f:
            json.dump([], f)

    if not os.path.exists(VICTIMS_FILE):
        with open(VICTIMS_FILE, "w") as f:
            json.dump([], f)

init_files()

# ---------- LOAD SAVE ----------
def load_camps():
    with open(CAMPS_FILE) as f:
        return json.load(f)

def save_camps(data):
    with open(CAMPS_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_victims():
    with open(VICTIMS_FILE) as f:
        return json.load(f)

def save_victims(data):
    with open(VICTIMS_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ---------- HOME ----------
@app.route("/")
def home():
    return "Backend Running"

# ---------- ADD CAMP ----------
@app.route("/add_camp", methods=["POST"])
def add_camp():
    data = request.json or {}
    camps = load_camps()

    if not data.get("camp_id"):
        return jsonify({"message": "Camp ID required"})

    new_camp = {
        "camp_id": data.get("camp_id"),
        "location": data.get("location"),
        "capacity": int(data.get("capacity", 0)),
        "food_packets": int(data.get("food_packets", 0)),
        "medical_kits": int(data.get("medical_kits", 0)),
        "volunteers": int(data.get("volunteers", 0)),
        "occupied": 0
    }

    camps.append(new_camp)
    save_camps(camps)

    return jsonify({"message": "Camp added successfully"})

# ---------- REGISTER ----------
@app.route("/register_victim", methods=["POST"])
def register_victim():
    data = request.json or {}

    victims = load_victims()
    camps = load_camps()

    for camp in camps:
        if camp["camp_id"] == data.get("camp_id"):

            if camp["occupied"] >= camp["capacity"]:
                return jsonify({"message": "Camp is full"})

            camp["occupied"] += 1

            victim = {
                "victim_id": data.get("victim_id"),
                "name": data.get("name"),
                "age": int(data.get("age", 0)),
                "health": data.get("health", "normal"),
                "camp_id": data.get("camp_id")
            }

            victims.append(victim)

            save_victims(victims)
            save_camps(camps)

            return jsonify({"message": "Victim registered successfully"})

    return jsonify({"message": "Camp not found"})

# ---------- GET ----------
@app.route("/get_camps")
def get_camps():
    return jsonify(load_camps())

@app.route("/get_victims")
def get_victims():
    return jsonify(load_victims())

# ---------- SEARCH ----------
@app.route("/search_victim/<vid>")
def search_victim(vid):
    for v in load_victims():
        if v["victim_id"] == vid:
            return jsonify(v)
    return jsonify({"message": "Victim not found"})

# ---------- DELETE ----------
@app.route("/remove_victim/<vid>", methods=["DELETE"])
def remove_victim(vid):
    victims = load_victims()
    camps = load_camps()

    victim = next((v for v in victims if v["victim_id"] == vid), None)

    if not victim:
        return jsonify({"message": "Victim not found"})

    for camp in camps:
        if camp["camp_id"] == victim["camp_id"]:
            camp["occupied"] -= 1

    victims = [v for v in victims if v["victim_id"] != vid]

    save_victims(victims)
    save_camps(camps)

    return jsonify({"message": "Victim deleted successfully"})

# ---------- REPORT ----------
@app.route("/report")
def report():
    camps = load_camps()
    victims = load_victims()

    return jsonify({
        "total_camps": len(camps),
        "total_victims": len(victims),
        "critical_victims": len([v for v in victims if v["health"] == "critical"]),
        "highest_occupancy_camp": max(camps, key=lambda x: x["occupied"], default={"camp_id":"None"})["camp_id"]
    })

if __name__ == "__main__":
    app.run(debug=True)