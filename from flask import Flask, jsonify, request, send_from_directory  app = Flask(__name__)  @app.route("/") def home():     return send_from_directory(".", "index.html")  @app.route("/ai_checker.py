from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/check", methods=["POST"])
def check():
    return jsonify({
        "ai_probability": "0%"
    })

if __name__ == "__main__":
    app.run(port=5000)
