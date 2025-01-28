import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load student data from JSON file
with open("q-vercel-python.json", "r") as f:
    students = json.load(f)

# API route to fetch marks by names
@app.route("/api", methods=["GET"])
def get_student_marks():
    # Get names from query parameters
    names = request.args.getlist("name")
    
    # Fetch marks for the requested names
    result = {name: next((student["marks"] for student in students if student["name"] == name), None) for name in names}
    
    return jsonify(result)
