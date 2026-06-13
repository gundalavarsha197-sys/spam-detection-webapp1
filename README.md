# 📧 Phishing Email Detection Web App

A Machine Learning-based web application that detects whether an email is Phishing or Safe using Natural Language Processing (NLP) and Scikit-learn, deployed using Flask.

## 🚀 Live Demo
https://your-live-link-here.com

## 📌 Project Overview
This project uses machine learning to classify emails as phishing or safe based on their content. It applies NLP techniques like TF-IDF for feature extraction and uses a trained ML model deployed with Flask to provide real-time predictions through a web interface.

## ✨ Features
- Real-time email classification
- Detects phishing and safe emails
- NLP-based text processing using TF-IDF
- Machine learning prediction
- Simple and responsive web interface

## 🛠️ Tech Stack
Python, Flask, Scikit-learn, Pandas, NumPy, HTML, CSS

## 🧠 Workflow
Dataset collection → Data preprocessing → Feature extraction (TF-IDF) → Model training → Evaluation → Flask deployment

## 📁 Project Structure
spam-detection-webapp/  
app.py  
model.pkl  
vectorizer.pkl  
requirements.txt  
templates/ (HTML files)  
static/ (CSS files)  
README.md  

## 💻 How to Run
Clone the repository → Install requirements using pip install -r requirements.txt → Run python app.py → Open http://127.0.0.1:5000 in browser

## 📸 Output
Input email text → Model predicts whether it is Phishing or Safe
<img width="1918" height="1078" alt="Screenshot 2026-06-13 152313" src="https://github.com/user-attachments/assets/13c8d241-da0f-4c56-b692-41fb9d00c6f3" />


## 📈 Example
“Win free iPhone now” → Phishing 🚨  
“Meeting scheduled at 10 AM” → Safe ✅

## 🌐 Deployment
Can be deployed using Render, Railway, or Heroku

## 👨‍💻 Author
GUNDALA VARSHA

## ⭐ Future Improvements
Improve accuracy using deep learning, add URL detection, enhance UI, and deploy with a custom domain

## 🏆 Conclusion
This project demonstrates a real-world application of machine learning in cybersecurity by detecting phishing emails with high accuracy using NLP and Flask.
