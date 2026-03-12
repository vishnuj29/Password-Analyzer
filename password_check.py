from flask import Flask, render_template, request
import re
import hashlib
import requests

app = Flask(__name__)

def check_strength(password):
    feedback = []
    
    if len(password) < 14:
        feedback.append("Use at least 14 characters")
    if not re.search(r"[A-Z]", password):
        feedback.append("Add uppercase letter")
    if not re.search(r"[a-z]", password):
        feedback.append("Add lowercase letter")
    if not re.search(r"\d", password):
        feedback.append("Add number")
    if not re.search(r"[!@#$%^&*()_+=]", password):
        feedback.append("Add special character")

    return feedback


def check_breach(password):
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    res = requests.get(url)

    for line in res.text.splitlines():
        h, count = line.split(":")
        if h == suffix:
            return f"Password found in breaches {count} times"

    return "Password not found in breaches"


@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    feedback = []

    if request.method == "POST":
        password = request.form["password"]
        feedback = check_strength(password)
        result = check_breach(password)

    return render_template("index.html", feedback=feedback, result=result)


if __name__ == "__main__":
    app.run(debug=True)