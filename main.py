from flask import Flask, render_template, redirect, request
from sqlalchemy_pagination import paginate
from message import Message, db
import constants


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():

    page = request.args.get("page")
    if not page:
        page = 1

    messages_query = db.query(Message)
    messages = paginate(query=messages_query, page=int(page), page_size=constants.PAGE_NUMBER)

    return render_template("index.html", messages=messages)


@app.route("/message-handler", methods=["POST"])
def message_handler():
    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    email = request.form.get("email")
    message = request.form.get("message")

    contact_message = Message(first_name=first_name, last_name=last_name,
                              email=email, message=message)
    contact_message.save()

    return redirect("/")


if __name__ == "__main__":
    app.run(port=5002, use_reloader=True)
