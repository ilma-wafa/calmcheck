from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/feel", methods=["POST"])
def feel():
    emotion = request.form.get("emotion")

    if emotion == "sad":
        message = "Thank you for sharing that. You don’t have to carry it alone."

    return render_template("index.html", response=message)

if __name__ == "__main__":
    app.run(debug=True)
