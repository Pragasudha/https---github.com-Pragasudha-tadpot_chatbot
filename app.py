from flask import Flask, render_template, request
from chatbot import get_bot_response
from db import init_db

app = Flask(__name__)
init_db()

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/chat", methods=["POST"])
def chat_page():
    role = request.form.get("role")
    return render_template("chat.html", role=role)

@app.route("/get", methods=["GET"])
def get_message():
    user_input = request.args.get("msg")
    return get_bot_response(user_input)

if __name__ == "__main__":
    app.run(debug=True)


