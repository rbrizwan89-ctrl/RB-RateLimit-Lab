from flask import Flask, render_template, request, redirect, session
import time

app = Flask(__name__)
app.secret_key = "rate-limit-lab"

# Mock Database
USERS = {
    "student": "password123"
}

# Store Attempts
ATTEMPTS = {}

# Settings
MAX_ATTEMPTS = 3
BLOCK_TIME = 20  # seconds


@app.route("/")
def home():
    if "user" in session:
        return redirect("/dashboard")
    return redirect("/login")


# ------------------------
# VULNERABLE LOGIN (NO RATE LIMIT)
# ------------------------
@app.route("/login-vulnerable", methods=["GET", "POST"])
def login_vulnerable():
    error = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in USERS and USERS[username] == password:
            session["user"] = username
            return redirect("/dashboard")

        error = "Invalid credentials! (Try brute-forcing 😈)"

    return render_template("login.html", error=error, vulnerable=True)


# ------------------------
# SECURE LOGIN (RATE LIMIT)
# ------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    ip = request.remote_addr

    if ip not in ATTEMPTS:
        ATTEMPTS[ip] = {"count": 0, "blocked_until": 0}

    attempt = ATTEMPTS[ip]

    # Check block status
    if attempt["blocked_until"] > time.time():
        return render_template("blocked.html",
                               wait=round(attempt["blocked_until"] - time.time()))

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in USERS and USERS[username] == password:
            session["user"] = username
            attempt["count"] = 0
            return redirect("/dashboard")

        attempt["count"] += 1

        if attempt["count"] >= MAX_ATTEMPTS:
            attempt["blocked_until"] = time.time() + BLOCK_TIME
            return render_template("blocked.html", wait=BLOCK_TIME)

        error = f"Invalid! Attempts: {attempt['count']}/{MAX_ATTEMPTS}"

    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")
    return render_template("dashboard.html", user=session["user"])
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
