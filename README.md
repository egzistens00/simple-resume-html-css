![AWS](https://img.shields.io/badge/Built%20on-AWS-orange)

# 💼 Alif Danial | Cloud Resume, Feedback API & Visitor Logs

This is a full-stack cloud project where I built and deployed my own resume website, added a feedback system using Flask, and implemented visitor logging using AWS Lambda@Edge. Everything is deployed and working live in the cloud using AWS services.

---

## 🌐 Live Website

**🔗 Visit Resume:** [alifdanialresume.online](https://alifdanialresume.online)

---

---

## 🚀 Features

- ✅ Static resume website hosted on **AWS S3** and delivered via **CloudFront**
- ✅ Feedback form using **Flask API** hosted on **EC2**
- ✅ Feedback entries stored in **DynamoDB**
- ✅ Visitor tracking using **Lambda@Edge** (real-time page view logs)
- ✅ **CI/CD pipeline** with GitHub Actions for automatic S3 deployment

---

## 🧪 Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Flask), Flask-CORS
- **DevOps:** GitHub Actions, EC2, IAM
- **Cloud Services:**
  - Amazon S3 (hosting)
  - CloudFront (global distribution)
  - Lambda@Edge (visitor logging)
  - DynamoDB (data storage)
  - EC2 (Flask API hosting)

---

## 📤 How Everything Works

1. User visits the website → **CloudFront** delivers content from **S3**
2. Visitor’s IP and browser details → **Lambda@Edge** → stored in **DynamoDB**
3. Feedback form submission → sent to **Flask API** → stored in **DynamoDB**

---

## ⚙️ Deployment Notes

### Feedback API
- Hosted on an EC2 Ubuntu instance
- Flask app runs on port 5000
- Made public using **Cloudflare Tunnel** at `https://api.alifdanialresume.online`

### Visitor Logger (Lambda@Edge)
- Triggered on every request through CloudFront
- Logs IP address, user-agent, and timestamp to a DynamoDB table
- IAM roles and policies configured for secure access

---

## 💡 What I Learned

- Building and styling a personal site with HTML and CSS
- Hosting static sites on AWS S3 with CloudFront
- Creating backend APIs with Flask and deploying them on EC2
- Using **Cloudflare Tunnel** to expose local services securely
- Automating deployment with GitHub Actions
- Writing Lambda@Edge functions to log visitor info in real time
- Securing AWS services using IAM roles and trust policies

---

## 📸 Screenshots

> *You can add images later, like:*
- Homepage of your website
- DynamoDB entries (visitor logs and feedback)
- API terminal logs or Cloudflare dashboard

---

## 📬 Contact

- **Email:** alifdanial969@gmail.com  
- **LinkedIn:** [alifdanial969](https://www.linkedin.com/in/alifdanial969)  
- **GitHub:** [egzistens00](https://github.com/egzistens00)

---

> Built with 💻 HTML + ☁️ AWS + 🐍 Flask — by Alif Danial

