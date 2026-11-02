from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to DevOps Application!"


@app.route("/health")
def health():
    return jsonify({"status": "UP"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
