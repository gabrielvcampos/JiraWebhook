from flask import request
from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route("/api/v1/create_issue", methods=["POST"])
def create_issue():
    # data = request.json
    return "OK"


def iniciar_aplicacao():
    app.run(host='127.0.0.1', port=8080)


if __name__ == "__main__":
    iniciar_aplicacao()