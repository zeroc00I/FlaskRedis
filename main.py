"""The Flask App."""

# pylint: disable=broad-except

import json
from flask import Flask, abort, jsonify, request, render_template
from RedisQueue import RedisQueue

redisQueue = RedisQueue('test')
app = Flask(__name__)

@app.errorhandler(404)
def resource_not_found(exception):
    """Returns exceptions as part of a json."""
    return render_template('404.html'), 404
    return jsonify(
        error=str(exception)
        ), 404

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

            queueSize = countQueueSize().get_json().get('message')
            
            if (int(queueSize) > 0):
                messageValue = redisQueue.get()

                return jsonify(
                    message=f"{messageValue}",
                    success=True
                )
            else:
                return jsonify(
                    message=f"Nada para expurgar",
                    success=False
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
            message=f"Mensaje inserída en cola",
            success=True
        )

@app.route("/api/queue/count", methods=['GET'])
def countQueueSize():
    tamanho_fila = redisQueue.qsize()
    messageValue = f"{tamanho_fila}"
    
    if(int(messageValue) == 0):
        return jsonify(
            message=f"{messageValue}",
            success=False
        )

    else:

        return jsonify(
            message=f"{messageValue}",
            success=True
        )

@app.route("/api/queue/all", methods=['GET'])
def getAllFromQueue():
    return jsonify(
        messages=redisQueue.show_itens(),
        success=True
    )

if __name__ == "__main__":
    app.run(debug=True)
