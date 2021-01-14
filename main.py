"""The Flask App."""

# pylint: disable=broad-except

from flask import Flask, abort, jsonify, request
from RedisQueue import RedisQueue

redisQueue = RedisQueue('test')
app = Flask(__name__)

@app.errorhandler(404)
def resource_not_found(exception):
    """Returns exceptions as part of a json."""
    return jsonify(error=str(exception)), 404

@app.route("/")
def home():
    """Show the app is working."""
    return jsonify(
        message='APP is currently running'
        )

@app.route("/api/queue/pop" , methods=['POST'])
# Envia requisicao pra fila para
# Obter primeiro elemento da lista e Removê-lo
# Status Code esperado: 200 / 500
# Retorno: "message": "body del mensaje"
def queuePop():
    if request.method == "POST":

        messageValue = redisQueue.get()
        return jsonify(
        message=f"{messageValue}"
        )

@app.route("/api/queue/push", methods=['POST'])
# Envia requisicao pra fila para
# Adicionar nova mensagem para lista
# Status Code esperado: 200 / 404 / 500
# Retorno: {"message": "Pusheo un mensaje"}
def queueInsert():
    if request.method == "POST":
        messageValue = request.get_json().get('message','')

        if not messageValue:
            abort(
                404,
                description=(
                    "No query parameter messageValue passed. "
                    "Send a value to the messageValue query parameter."
                ),
            )
        redisQueue.put(messageValue)

        return jsonify(
        message=f"Pusheo un mesaje"
        )

@app.route("/api/queue/count", methods=['GET', 'POST'])
def countQueueSize():
    tamanho_fila = redisQueue.qsize()

    messageValue = f"{tamanho_fila}"
    
    return jsonify(
        message=f"{messageValue}"
        )

if __name__ == "__main__":
    app.run(debug=True)
