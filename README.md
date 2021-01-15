# Chall

![alt text](https://github.com/bminossi/FlaskRedis/blob/main/fotodepresentacion.png?raw=true)

## Tasks
- Consultar as mensagens em fila :heavy_check_mark:
- Manipular mensagens existentes (Push, Pop, Count) :heavy_check_mark:
- Manipular mensagens existentes através de rotas :heavy_check_mark:
- Implementar conceito de fila assíncrona com workers :x:
  - Durante o desenvolvimento do projeto houve uma mudança de estratágia quanto a necessidade do projeto possuir workers / estar preparado para ser consumido por outro sistema; Tendo em vista que o consumer é exclusivamente o visitante da página, que irá manpular a fila de mensagens, não viu-se necessidade de tal infraestrutura. 
- Desenvolver um client em JS para realizar o consumo da API rest desenvolvida :heavy_check_mark:
- Adaptar ambiente para Docker :heavy_check_mark:


## Fontes de conhecimento utilizadas
### Instalar Redis

https://dev.to/divshekhar/how-to-use-redis-with-python-1nd6

https://realpython.com/python-redis/

### Exemplos Flask + Redis

https://gist.github.com/swdevbali/f4adcacd402216256dd8

https://realpython.com/flask-by-example-implementing-a-redis-task-queue/

https://gist.github.com/calderonroberto/f4d8badb94c01e9020db

https://www.scaleway.com/en/docs/how-to-install-flask-on-your-server/


### Base de exemplo de conceitos de fila

https://towardsdatascience.com/use-redis-queue-for-asynchronous-tasks-in-a-flask-app-d39f2a8c2667

https://github.com/bee-queue/bee-queue (Somente adicionar tarefa na fila / Não processar ela automaticamente)

### Bypassing workers

For testing purposes, you can enqueue jobs without delegating the actual execution to a worker (available since version 0.3.1). To do this, pass the is_async=False argument into the Queue constructor:

https://python-rq.org/docs/#bypassing-workers

```
curl -X POST http://127.0.0.1:5000/enqueue -d '{"hello":"world"}'
{
  "job_id": "4dfd1d5b-cf3b-4366-83a8-afa4f5de5244"
}
```
```
http://127.0.0.1:5000/get_result?job_id=4dfd1d5b-cf3b-4366-83a8-afa4f5de5244

{
  "input": null, 
  "job_enqueued_at": "2021-01-14T00:55:23.500216", 
  "job_id": "4dfd1d5b-cf3b-4366-83a8-afa4f5de5244", 
  "job_started_at": "2021-01-14T00:57:42.565441", 
  "result": null
}
```
### Erros enfrentados e soluções encontradas
https://stackoverflow.com/questions/55770968/i-am-struggling-to-get-value-by-key-from-the-jsonify-object-in-python-flask

https://redis.io/commands/lrem

https://redis.io/commands/rpoplpush

https://realpython.com/flask-by-example-implementing-a-redis-task-queue/

http://peter-hoffmann.com/2012/python-simple-queue-redis-queue.html

https://python-rq.org/

https://pypi.org/project/redis_queue/

https://www.twilio.com/blog/asynchronous-tasks-in-python-with-redis-queue

https://kb.objectrocket.com/redis/create-a-simple-task-queue-with-flask-and-redis-1467







