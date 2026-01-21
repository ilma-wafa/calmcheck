from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start-chat", methods=["POST"])
def start_chat():
    data = request.json
    emotion = data.get("emotion")

    responses = {
        "sad": "I’m really glad you told me that. You don’t have to carry it alone.",
        "overwhelmed": "That sounds like a lot to hold at once. Let’s slow things down together.",
        "okay": "Thanks for checking in with yourself. Want to talk a bit more?",
        "unknown": "It’s okay not to have the words right now. We can take this gently."
    }

    message = responses.get(emotion, "I’m here with you.")

    return jsonify({"message": message})


@app.route("/continue-chat", methods=["POST"])
def continue_chat():
    return jsonify({
        "message": "Take your time. What’s been on your mind lately?"
    })


if __name__ == "__main__":
    app.run(debug=True)
