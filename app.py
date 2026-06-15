from flask import Flask, request, jsonify

from db import init_db, get_conn
from service import *

app = Flask(__name__)

init_db()

@app.route("/users", methods=["GET"])
def get_users():

    try:
        nome = request.args.get("nome")
        eta = request.args.get("eta")

        persone = lista_persone(nome, eta)

        return jsonify(persone), 200

    except Exception as e:
        return {"error": "errore server", "details": str(e)}, 500



@app.route("/users", methods=["POST"])
def create_user():

    try:
        data = request.json

        if not data.get("nome"):
            return {"error": "nome obbligatorio"}, 400

        if "eta" not in data or data["eta"] < 0:
            return {"error": "eta non valida"}, 400

        crea_persona(data["nome"], data["eta"])

        return {"status": "created"}, 201

    except Exception as e:
        return {"error": "errore server", "details": str(e)}, 500




@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):

    try:
        data = request.json

        ok, reason = modifica_persona(
            id,
            data.get("nome"),
            data.get("eta")
        )

        if not ok and reason == "not_found":
            return {"error": "utente non trovato"}, 404

        return {"status": "updated", "id": id}, 200

    except Exception as e:
        return {"error": "errore server", "details": str(e)}, 500



@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):

    try:
        ok, reason = elimina_persona(id)

        if not ok and reason == "not_found":
            return {"error": "utente non trovato"}, 404

        return {"status": "deleted", "id": id}, 200

    except Exception as e:
        return {"error": "errore server", "details": str(e)}, 500




if __name__ == "__main__":
    app.run(debug=True)
