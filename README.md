(https://github.com/user-attachments/files/21550196/README.1.md)
# 🚨 Incident Tracker

A full-stack incident tracking application built with **Flask**, **MongoDB Atlas**, and **HTML/CSS/JS**. This tool allows users to submit, store, and view incident reports via a modern web interface — ideal for internal monitoring or support workflows.

![GitHub repo size](https://img.shields.io/github/repo-size/nishanthsvbhat/incident-tracker)
![GitHub last commit](https://img.shields.io/github/last-commit/nishanthsvbhat/incident-tracker)
![MongoDB Atlas](https://img.shields.io/badge/Database-MongoDB%20Atlas-brightgreen)
![Flask](https://img.shields.io/badge/Backend-Flask-blue)
![License](https://img.shields.io/github/license/nishanthsvbhat/incident-tracker)

---

## 🌟 Features

- 🔐 Secure backend with Flask and RESTful API
- 📄 Incident creation with title, description, and timestamp
- 📦 MongoDB Atlas for remote data storage
- 🧭 API endpoint to fetch incident data (`/api/incidents`)
- 🌐 Deployed on Render for easy access

---

## 🚀 Live Demo

🌍 [Visit Live App](https://incident-tracker-8jmd.onrender.com)

---

## 🏗️ Tech Stack

| Layer       | Technology        |
|-------------|-------------------|
| Frontend    | HTML, CSS, JavaScript |
| Backend     | Python (Flask)    |
| Database    | MongoDB Atlas     |
| Deployment  | Render.com        |

---

## 📁 Project Structure

```bash
incident-tracker/
├── backend/
│   ├── app.py             # Flask backend logic
│   ├── .env               # MongoDB URI (use dotenv)
├── frontend/
│   ├── index.html         # UI Form
│   ├── script.js          # Fetch + POST incidents
│   ├── style.css          # Styling
├── requirements.txt
└── README.md
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/nishanthsvbhat/incident-tracker.git
cd incident-tracker
```

### 2. Setup Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r ../requirements.txt
```

### 3. Set Up MongoDB Atlas

- Create a free cluster at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- Whitelist your IP (`0.0.0.0/0`)
- Create a DB user (e.g., `incidentUser`)
- Create a database named `incidentDB`
- Format your Mongo URI like:

```bash
MONGO_URI=mongodb+srv://incidentUser:<password>@cluster0.mongodb.net/incidentDB?retryWrites=true&w=majority&appName=Cluster0
```

- Add to `.env` file:

```
MONGO_URI=your_full_connection_string
```

### 4. Run the Flask App

```bash
python app.py
```

Your backend will run on `http://localhost:5000`.

### 5. Open the Frontend

Open `frontend/index.html` in your browser and submit an incident!

---

## 🧪 API Endpoint

- `GET /api/incidents` – fetch all incidents
- `POST /api/incidents` – submit a new incident

---

## 📷 Screenshots

![Form UI](https://raw.githubusercontent.com/nishanthsvbhat/incident-tracker/main/screenshots/form_ui.png)
![Incident Submission](https://raw.githubusercontent.com/nishanthsvbhat/incident-tracker/main/screenshots/api_response.png)

---

## ✅ Future Improvements

- 🔐 Add authentication
- 📊 Admin dashboard to view/filter incidents
- ✉️ Email notifications for submissions
- 📱 Make UI responsive

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📄 License

[MIT](https://choosealicense.com/licenses/mit/)

---

## ✨ Author

Made with ❤️ by [Nishanth SV Bhat](https://github.com/nishanthsvbhat)
