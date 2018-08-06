from flask import request
from flask import Flask
from flask import jsonify
from flasgger import Swagger


app = Flask(__name__)
Swagger = Swagger(app)



@app.route("/api/v1/create_issue", methods=["POST"])
def create_issue():
    data = str(request.json)
    
    if data is not None:
        print(data)
        return jsonify(data)
    return "OK"


def iniciar_aplicacao():
    app.run(host='127.0.0.1', port=8080, debug=True)


if __name__ == "__main__":
    iniciar_aplicacao()