
from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary in-memory storage
users = {}
courses = ["Web Development", "Python", "Database"]
enrollments = {}

# 🟢 Home Route
@app.route('/')
def home():
    return "E-Learning Backend Running"

# 🟢 Signup
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username in users:
        return jsonify({"message": "User already exists"}), 400

    users[username] = password
    enrollments[username] = []

    return jsonify({"message": "Signup successful"})

# 🟢 Login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if users.get(username) == password:
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid credentials"}), 401

# 🟢 Get Courses
@app.route('/courses', methods=['GET'])
def get_courses():
    return jsonify(courses)

# 🟢 Enroll Course
@app.route('/enroll', methods=['POST'])
def enroll():
    data = request.json
    username = data.get('username')
    course = data.get('course')

    if course not in courses:
        return jsonify({"message": "Course not found"}), 404

    if course not in enrollments[username]:
        enrollments[username].append(course)

    return jsonify({"message": "Enrolled successfully"})

# 🟢 Get My Courses
@app.route('/mycourses/<username>', methods=['GET'])
def my_courses(username):
    return jsonify(enrollments.get(username, []))

# 🟢 Run Server
if __name__ == '__main__':
    app.run(debug=True)
