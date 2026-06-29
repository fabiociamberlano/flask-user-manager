# Flask User Manager

A simple REST API built with **Flask** and **SQLite** for managing users.

This project was created as part of my learning path in backend development, focusing on REST APIs, database integration, and software architecture.

---

## 🚀 Features

- Create a user (POST /users)
- Get all users (GET /users)
- Update a user (PUT /users/<id>)
- Delete a user (DELETE /users/<id>)
- Filter users by query parameters
- Input validation
- Error handling

---

## 🛠 Tech Stack

- Python
- Flask
- SQLite
- SQL
- Git & GitHub

---

## 📁 Project Structure

```
app.py          # API routes
service.py      # Business logic
db.py           # Database connection
client.py       # Test client
```

---

## ▶️ How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
python app.py
```

3. API will be available at:

```
http://127.0.0.1:5000
```

---

## 📌 Example Requests

### Create user

```http
POST /users
Content-Type: application/json

{
  "nome": "Luca",
  "eta": 30
}
```

---

### Get users

```http
GET /users
```

---

### Update user

```http
PUT /users/1
Content-Type: application/json

{
  "nome": "Marco",
  "eta": 35
}
```

---

### Delete user

```http
DELETE /users/1
```

---

## 🧠 What I Learned

- How REST APIs work
- CRUD operations
- Flask routing
- SQLite integration
- Separation of concerns (app / service / db)
- Error handling
- Git workflow (branch, commit, PR)

---

## 📈 Future Improvements

- Add authentication
- Migrate to PostgreSQL
- Add Flask Blueprints
- Improve validation layer
- Add automated tests

---

## 👤 Author

- GitHub: https://github.com/fabiociamberlano/fabiociamberlano
- LinkedIn: https://www.linkedin.com/in/fabiociamberlano/
