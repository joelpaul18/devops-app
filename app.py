from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to DevOps Application! - Development!"


@app.route("/health")
def health():
    return jsonify({"status": "UP"})

@app.route("/about")
def about():
    return "This is a Flask application for DevOps practical lab."

@app.route("/version")
def version():
    return jsonify({"version": "1.0.0"})

@app.route("/contact")
def contact():
    return jsonify({
        "email": "joelpaul@gmail.com",
        "team": "DevOps Team"
    })

@app.route("/status")
def status():
    return jsonify({
        "application": "running",
        "environment": "development"
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
