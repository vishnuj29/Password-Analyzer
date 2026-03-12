# 🔐 Password Security Analyzer

A **Cybersecurity Web Tool** that analyzes password strength and checks whether a password has appeared in known data breaches. This project helps users create **strong and secure passwords** by providing real-time feedback and breach detection.

The application is built using **Python and Flask** and provides a **modern cybersecurity dashboard interface**.

---

# 📌 Project Overview

Passwords are one of the most common targets for cyber attacks. Many users reuse weak or compromised passwords, which makes their accounts vulnerable.

This tool performs two main security checks:

- **Password Strength Analysis**
- **Breach Detection using leaked password databases**

The system warns users if their password is weak or has appeared in previous data breaches.

---

# ⚙️ Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Regex
- Have I Been Pwned API

---

# 🚀 Features

## 🔐 Password Strength Checker

The system analyzes the password based on security rules:

- Minimum 14 characters
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

A **visual strength meter** indicates password strength.

---

## ⚠ Breach Detection

The tool checks whether the password has appeared in known data breaches.

If the password exists in leaked datasets, the system displays a warning.

Example output:

```
Password found in breaches 80942123 times
```

---

## 🟥🟨🟩 Password Strength Meter

A dynamic security meter shows the strength level:

- 🔴 Weak
- 🟡 Medium
- 🟢 Strong

---

## 👁 Show / Hide Password

Users can toggle password visibility to verify what they typed.

---

## 🎲 Secure Password Generator

The tool can automatically generate a **strong 14-character password** containing:

- Letters
- Numbers
- Special symbols

---

## 🌐 Cybersecurity Dashboard UI

The project includes a modern dark-themed interface designed like a **security dashboard**.

---

# 🧠 How It Works

1. User enters a password.
2. The system analyzes password strength using **regex validation**.
3. The password is converted into a **SHA-1 hash**.
4. The hash is checked against the **Have I Been Pwned** database using the **k-anonymity model**.
5. The system displays:
   - Security feedback
   - Breach detection result
   - Strength meter visualization

---

# 📂 Project Structure


password-security-analyzer
│
├── password_check.py
│── index.html
├── requirements.txt
└── README.md

---

# ▶️ How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/yourusername/password-security-analyzer.git
```

### 2. Navigate to the project folder

```
cd password-security-analyzer
```

### 3. Create a virtual environment

```
python3 -m venv venv
```

### 4. Activate the environment

```
source venv/bin/activate
```

### 5. Install dependencies

```
pip install -r requirements.txt
```

### 6. Run the application

```
python password_check.py
```

### 7. Open the browser

```
http://127.0.0.1:5000
```

---

# 📊 Example Use Case

If a weak password like **12345678** is entered:

- The system will show security feedback
- It will detect if the password exists in known breaches
- It will recommend creating a stronger password

---

# 🔒 Cybersecurity Concepts Demonstrated

This project demonstrates several important cybersecurity concepts:

- Password security
- Data breach detection
- Hashing (SHA-1)
- API integration
- Secure password practices

---

# 📈 Future Improvements

Possible enhancements for this project:

- Password entropy calculator
- Security risk score
- Dark web breach monitoring
- Advanced cybersecurity dashboard
- User authentication system

---

# 👨‍💻 Author

Developed as a **Cybersecurity Practical Project** to demonstrate password security analysis and breach detection.
---
# 📸 Screenshot
![image_alt](https://github.com/vishnuj29/Password-Analyzer/blob/e5dbb418a4b5c8127a45cc6a5d43da19327412d7/Screenshot_2026-03-12_11_20_16.png)
![image_alt](https://github.com/vishnuj29/Password-Analyzer/blob/e5dbb418a4b5c8127a45cc6a5d43da19327412d7/Screenshot_2026-03-12_11_18_59.png)
