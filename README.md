REST API for User Management

## 🎯 Objective
Create a **Flask-based REST API** to manage user data with full CRUD functionality.

---

## 🧰 Tools Used
- Python 3
- Flask
- Curl (for testing)

Install dependencies:
```bash
pip install flask
```

---

## 🚀 How to Run
```bash
python app.py
```
The server will start at:
```
http://127.0.0.1:5000/
```

---

## 🧩 API Endpoints

| Method | Endpoint | Description |
|---------|-----------|-------------|
| GET | `/users` | Retrieve all users |
| GET | `/users/<id>` | Retrieve specific user |
| POST | `/users` | Add a new user |
| PUT | `/users/<id>` | Update user details |
| DELETE | `/users/<id>` | Delete a user |

---

## 🧪 Example Using Curl

```bash
# Add User
curl -X POST -H "Content-Type: application/json" -d '{"name":"Alice","email":"alice@example.com"}' http://127.0.0.1:5000/users

# Get All Users
curl http://127.0.0.1:5000/users

# Update User
curl -X PUT -H "Content-Type: application/json" -d '{"email":"alice_new@example.com"}' http://127.0.0.1:5000/users/1

# Delete User
curl -X DELETE http://127.0.0.1:5000/users/1
```

---

## 🏁 Outcome
✅ Learn the fundamentals of REST API development:
- CRUD operations  
- JSON handling  
- API testing with Postman or Curl  
