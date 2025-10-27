from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage
users = {}

# ✅ Homepage route
@app.route('/')
def home():
    return """
    <h2>Welcome to the User Management API 🚀</h2>
    <p>Use the following endpoints:</p>
    <ul>
        <li>GET /users — Retrieve all users</li>
        <li>GET /users/&lt;id&gt; — Retrieve specific user</li>
        <li>POST /users — Add a new user</li>
        <li>PUT /users/&lt;id&gt; — Update user</li>
        <li>DELETE /users/&lt;id&gt; — Delete user</li>
    </ul>
    """

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"message": "User not found"}), 404

# POST - Add new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = len(users) + 1
    users[user_id] = data
    return jsonify({"id": user_id, "message": "User added successfully"}), 201

# PUT - Update user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        data = request.get_json()
        users[user_id].update(data)
        return jsonify({"message": "User updated successfully"})
    return jsonify({"message": "User not found"}), 404

# DELETE - Remove user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted successfully"})
    return jsonify({"message": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
R