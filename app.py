
from flask import Flask, jsonify

app = Flask(__name__)

pets = [
    {
        "id": 1,
        "name": "Bruno",
        "type": "Dog",
        "age": 3,
        "vaccinated": True
    },
    {
        "id": 2,
        "name": "Kitty",
        "type": "Cat",
        "age": 2,
        "vaccinated": True
    }
]


@app.route("/")
def home():
    return "Welcome to the Pet Care Management System!"


@app.route("/pets")
def get_pets():
    return jsonify(pets)


@app.route("/pets/<int:pet_id>")
def get_pet(pet_id):
    pet = next((p for p in pets if p["id"] == pet_id), None)

    if pet is None:
        return jsonify({"error": "Pet not found"}), 404

    return jsonify(pet)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
