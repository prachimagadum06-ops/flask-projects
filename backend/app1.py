from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb+srv://mtanvi528_db_user:mtanvi528_db_user@cluster0.ye0o5h5.mongodb.net/?appName=Cluster0")
db = client["todo_database"]
collection = db["todo_items"]

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    data = request.get_json()

    item_name = data.get("itemName")
    item_description = data.get("itemDescription")

    collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })

    return jsonify({
        "message": "To-Do item submitted successfully"
    }), 201

if __name__ == "__main__":
    app.run(debug=True, port=5000)