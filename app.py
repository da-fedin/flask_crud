from flask import Flask
from webargs import fields
from webargs.flaskparser import use_args

from application.services import print_output
from application.services.user_generator import generate_users

app = Flask(__name__)


@app.route("/get-content")
def print_file(file_name="some_input.txt") -> str | None:
    # Handle input - start.
    file_to_print = file_name
    # Handle input - end.

    # Handle logic - start.
    output = print_output(file_to_print)
    # Handle logic - end.

    return output


@app.route("/generate-users")
@use_args({"amount": fields.Int(missing=20)}, location="query")
def users_generate(args) -> str:
    # Handle input - start.
    amount = args["amount"]
    # Handle input - end.

    # Handle logic - start.
    users = generate_users(amount=amount)
    # Handle logic - end.

    users_formatted = []

    for user in users:
        user_formatted = (
            f"<li><span>{user.name}</span> - <span>{user.email}</span></li>"
        )
        users_formatted.append(user_formatted)

    item = "".join(users_formatted)
    return f"<ul>{item}</ul>"


if __name__ == "__main__":
    app.run()
