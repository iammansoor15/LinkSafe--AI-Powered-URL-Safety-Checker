# 🔗 LinkSafe – AI-Powered URL Safety Checker

**LinkSafe** is a machine learning-powered phishing URL detection tool with a Flask backend and React frontend. It helps users check if a URL is **safe** or **malicious** in real time.

🔗 **Live App**: [https://linksafe-ai-powered-url-safety-checker.onrender.com/](https://linksafe-ai-powered-url-safety-checker.onrender.com/)

---

## 🚀 Features

- ✅ Real-time phishing URL detection  
- 🧠 Machine learning model for smart predictions  
- 🌐 React-based user interface  
- ⚙️ Flask backend with RESTful API  
- 📊 Confidence scores for predictions  

---

## 📦 Installation

### 🔙 Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate     # Use 'source venv/bin/activate' on macOS/Linux
pip install -r requirements.txt
python app.py
```

The Flask server will start at `http://localhost:5000`

---

### 🖥️ Frontend Setup

In a new terminal:

```bash
cd frontend
npm install
npm start
```

React app will run at `http://localhost:3000`

---

## 🌐 How to Use

1. Visit the live app:  
   [https://linksafe-ai-powered-url-safety-checker.onrender.com/](https://linksafe-ai-powered-url-safety-checker.onrender.com/)
2. Enter the URL you want to check.
3. Click **Scan URL**.
4. View the result: "Safe" or "Phishing" with a confidence score.

---

## 🧠 How It Works

- The backend extracts features from the input URL (length, special characters, etc.)
- A trained machine learning model classifies the URL.
- The prediction is returned to the React frontend via API.
- The frontend displays the result to the user.

---

## 🗂️ Project Structure

```
LinkSafe/
├── backend/
│   ├── __pycache__/
│   ├── dataset/
│   ├── models/
│   ├── notebooks/
│   │   ├── __pycache__/
│   │   ├── Feature_Extraction.py
│   │   └── Phishing_URL.ipynb
│   ├── venv/
│   ├── app.py
│   ├── Procfile
│   ├── requirements.txt
│   ├── package-lock.json
│   └── package.json
│
├── frontend/
│   ├── node_modules/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   │   ├── LinkSafe.png
│   │   │   ├── logo_back.jpg
│   │   │   └── warning.png
│   │   ├── Home/
│   │   │   ├── home.css
│   │   │   └── Home.jsx
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   ├── .gitignore
│   ├── eslint.config.js
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   ├── README.md
│   └── vite.config.mjs
```

---

