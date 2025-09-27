from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def echo():
    return jsonify({
        "message": "Mock backend is running!",
        "method": request.method,
        "args": request.args,
        "json": request.get_json(silent=True)
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
