![AWS](https://img.shields.io/badge/Built%20on-AWS-orange)

# 💼 Alif Danial - Cloud Resume + Feedback API + Visitor Logs

This is a complete full-stack cloud project portfolio combining frontend, backend, and AWS infrastructure skills. Everything here is real, deployed, and working.

---

## 🌐 Live Site
**Resume Website:** [alifdanialresume.online](https://alifdanialresume.online)

---

## 🧱 Project Structure
```
.
├── index.html                ← Resume website (HTML + Feedback Form)
├── style.css                 ← Styling for resume
├── aaku.png                  ← Profile photo
│
├── feedback-api/             ← Flask backend API for feedback form
│   ├── app.py                ← Handles POST requests + writes to DynamoDB
│   └── requirements.txt      ← Flask, boto3, flask-cors
│
├── visitor-analytics/        ← Lambda@Edge function for logging visitors
│   └── lambda_function.js    ← Stores IP/user-agent to DynamoDB
│
└── README.md                 ← This file
```

---

## 🚀 Features
- ✅ **HTML Resume Website** hosted on AWS S3 + CloudFront
- ✅ **Visitor Feedback Form** connected to Flask API on EC2
- ✅ **DynamoDB** table to store feedback data
- ✅ **Visitor Logging System** using Lambda@Edge to track real-time page views
- ✅ **CI/CD Deployment** from GitHub to S3 via GitHub Actions

---

## 🧪 Tech Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Flask), Flask-CORS, Docker (optional)
- **DevOps:** GitHub Actions, EC2, IAM
- **AWS Services:**
  - S3, CloudFront
  - Lambda@Edge
  - DynamoDB
  - EC2 (Ubuntu)

---

## 📤 How It Works
### 1. User opens the website → **CloudFront** delivers content
### 2. Visitor info (IP, user-agent) → **Lambda@Edge** → **DynamoDB** `visitorLogs`
### 3. Visitor submits feedback → **Flask API** → **DynamoDB** `feedbackData`

---

## 📂 Deployment Notes
### Feedback API:
- Hosted on EC2
- Flask exposed on port 5000
- Tunnelled using **Cloudflare Tunnel** to custom domain `api.alifdanialresume.online`

### Lambda@Edge:
- JS code triggered on every viewer request
- Logs data into DynamoDB with `PutItem` operation

---

## 🧠 What I Learned
- Configuring IAM roles with precise DynamoDB permissions
- Working with Flask + AWS SDK (boto3)
- Hosting full-stack apps on AWS
- Monitoring HTTP logs and debugging permissions via EC2

---

## 📸 Screenshots
(Add screenshots here of:
- your deployed site,
- API console logs,
- DynamoDB tables showing visitor/feedback entries)

---

## 👋 Contact
**Email:** alifdanial969@gmail.com  
**LinkedIn:** [alifdanial969](https://www.linkedin.com/in/alifdanial969)

---

> Built with 💻, ☁️, and 🔥 by Alif Danial
