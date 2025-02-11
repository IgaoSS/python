# pylint: disable=E0401
from datetime import datetime, timedelta, timezone
import jwt # type: ignore
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def login():
    # Criação de um token JWT
    token = jwt.encode(
        payload = {
            'exp': datetime.now(timezone.utc) + timedelta(minutes=1),
            'iat': datetime.now(timezone.utc)
        },
        key="minhaChave",
        algorithm="HS256"
    )
    return jsonify({ "token": token }), 200

@app.route("/secret", methods=["POST"])
def secret():
    raw_token = request.headers.get("Authorization")
    print()
    print(raw_token)

    token = raw_token.split()[1]
    print()
    print(token)

    try:
        token_information = jwt.decode(token, key="minhaChave", algorithms="HS256")
        print()
        print(token_information)
    except Exception as exception:
        return jsonify({ "erro": str(exception) }), 400

    return jsonify({ "message": token_information }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)