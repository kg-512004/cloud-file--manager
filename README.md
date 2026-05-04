# ☁️ Cloud File Manager

A web-based cloud file management system built using Flask that allows users to upload, manage, and organize files through a simple and intuitive interface.

---

## 🚀 Features

* 📁 Upload files to server
* 📥 Download stored files
* 🗑️ Delete files
* 📂 Organize files via web interface
* 🌐 Accessible through browser
* ⚡ Lightweight and fast

---

## 🧠 Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS, JavaScript, Jinja2
* **Deployment:** Docker, Nginx

---

## 📂 Project Structure

```
cloud-file-manager/
│── static/          # CSS, JS, images
│── templates/       # HTML templates (Jinja2)
│── app.py           # Main Flask application
│── requirements.txt # Python dependencies
│── Dockerfile       # Docker configuration
│── docker-compose.yml
│── nginx.conf       # Nginx configuration
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/kg-512004/cloud-file-manager.git
cd cloud-file-manager
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application

```bash
python app.py
```

### 4️⃣ Open in browser

```
http://localhost:5000
```

---

## 🐳 Run with Docker (Recommended)

```bash
docker-compose up --build
```

---

## 📸 Screenshots

*(Add screenshots here for better presentation)*

---

## 🔒 Future Improvements

* User authentication (login/signup)
* Cloud storage integration (AWS S3 / Firebase)
* File sharing via links
* Database integration for metadata
* Drag & drop file upload

---

## 📌 Learning Outcomes

* Hands-on experience with Flask backend development
* Understanding of MVC-like architecture using templates
* Deployment using Docker and reverse proxy using Nginx
* File handling in web applications

---

## 🤝 Contributing

Feel free to fork this repository and contribute!

---

## 📧 Contact

* GitHub: https://github.com/kg-512004
