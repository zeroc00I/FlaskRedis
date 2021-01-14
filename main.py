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
    return "APP is currently running!"

@app.route("/get_result")
def get_result():
    """Takes a job_id and returns the job's result."""
    job_id = request.args["job_id"]

    try:
        job = Job.fetch(job_id, connection=redis_conn)
    except Exception as exception:
        abort(404, description=exception)

    if not job.result:
        abort(
            404,
            description=f"No result found for job_id {job.id}. Try checking the job's status.",
        )
    return jsonify(job.result)

@app.route("/api/queue/pop")
# Envia requisicao pra fila para
# Obter primeiro elemento da lista e Removê-lo
# Status Code esperado: 200 / 500
# Retorno: "message": "body del mensaje"

@app.route("/api/queue/push")
# Envia requisicao pra fila para
# Adicionar nova mensagem para lista
# Status Code esperado: 200 / 404 / 500
# Retorno: {"message": "Pusheo un mensaje"}
def queueInsert():
    try:
        if request.method == "GET":
            abort(407, description=exception)
        if request.method == "POST":
            messageValue = request.args["message"]
            redisQueue.put(messageValue)
    except Exception as exception:
        abort(407, description=exception)

@app.route("/api/queue/count")
# Checa quantas mensagens existem pendentes
# para processamento em fila
# Status Code esperado: 200 / 404
# Retorno: {"count": 351}
def count():
    queue = redis_queue
    count = len(queue.jobs)
    return f"Jobs in queue: {count}"

@app.route("/api/queue/allData")
def getAllData():
    tamanho_fila = redisQueue.qsize()
    return f"Tamanho fila: {tamanho_fila}"

if __name__ == "__main__":
    app.run(debug=True)
