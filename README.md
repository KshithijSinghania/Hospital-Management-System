# 🏥 Hospital Management System + 🧠 MediBot (AI Symptom Checker Chatbot)

An integrated full-stack Hospital Management System built with the **MERN stack (MongoDB, Express, React, Node.js)**, enhanced by **MediBot**, an AI-powered chatbot that assists patients by checking symptoms and suggesting nearby hospitals.

---

## 🚀 Overview

This web application streamlines hospital operations, including managing users (admins, doctors, patients), appointments, and medical records. It includes a smart chatbot, **MediBot**, that uses a PyTorch-trained model to provide preliminary symptom analysis and offline hospital recommendations based on location.

All components are combined into a single repository with three main folders:

- `backend` – Node.js + Express API
- `frontend` – React-based UI
- `chatbot` – Flask app with PyTorch model

---

## 🔗 Live Demo

- 🌐 <a href="https://hospital-management-sys-git-e1f527-kshithij-singhanias-projects.vercel.app" target="_blank">Frontend (Vercel)</a>  
- 🖥️ <a href="https://hospital-management-system-1dqr.onrender.com" target="_blank">Backend API (Render)</a>  
- 🤖 <a href="https://hospital-management-system-chatbot.onrender.com" target="_blank">MediBot Chatbot (Render)</a>

---

## ✨ Features

### 🏥 Hospital Management System

- 🔐 User authentication & authorization (Patients, Doctors, Admins)
- 📅 Appointment scheduling & patient record management
- 👨‍⚕️ Doctor dashboard with profile & availability
- 📊 Admin dashboard to manage users & hospital data
- 💻 Responsive UI for mobile and desktop

### 🤖 MediBot – AI Symptom Checker Chatbot

- 🧠 Intent classification using a PyTorch model
- 💬 Flask-powered chat interface embedded in the app
- 📍 Offline hospital lookup by area (e.g., “Kilpauk”, “Adyar”)
- 🧪 Terminal test version for debugging
- 📁 Static dataset (no external API calls required)

---

## 🛠️ Technologies Used

### Frontend

- React
- React Router
- Tailwind CSS
- Lucide Icons
- Axios

### Backend

- Node.js
- Express.js
- MongoDB & Mongoose
- JWT (JSON Web Token) for auth
- dotenv for environment config

### Chatbot

- Python
- Flask
- PyTorch
- scikit-learn
- Jinja2

---

## ⚙️ Getting Started (For Local Development)

### 📦 Prerequisites

- Node.js v14+
- Python 3.7+
- MongoDB (local or cloud)

---

## 📁 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/KshithijSinghania/Hospital-Management-System.git
cd Hospital-Management-System
```

---

### 2. Setup Backend (Node.js/Express)

```bash
cd backend
npm install
```

Create a `.env` file in `backend`:

```env
MONGO_URI=mongodb://0.0.0.0/Hospital-Management-System-MERN
PORT=8080
```

Optionally, create the first admin:

Edit `createAdmin.js`:

```js
const admin = new Admin({
  firstName: "abc",
  lastName: "xyz",
  email: "abc@gmail.com",
  password: "xyz123",
  role: "admin"
});
```

Run:

```bash
node createAdmin.js
```

Start server:

```bash
node server.js
```

---

### 3. Setup Frontend (React)

```bash
cd ../frontend
npm install
```

Create a `.env` file in `frontend`:

```env
REACT_APP_API_URL=https://your-backend-api.onrender.com
REACT_APP_CHATBOT_URL=https://your-chatbot-api.onrender.com
```

Start frontend:

```bash
npm start
```

Visit: [http://localhost:3000](http://localhost:3000)

---

### 4. Setup MediBot Chatbot (Flask)

```bash
cd ../chatbot
pip install -r requirements.txt
```

(Optional) To retrain the model:

```bash
python model/train.py
```

Run the chatbot:

```bash
python app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Chatbot Test CLI (Optional)

```bash
python test_chat.py
```

---

## 🧑‍💻 Contributing

Contributions are welcome! Feel free to:

- Submit a pull request 🛠️
- Open issues for bugs/suggestions 🐛
- Improve model training or expand the dataset 📊

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
