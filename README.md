# Chall

## Instalar Redis

https://dev.to/divshekhar/how-to-use-redis-with-python-1nd6

https://realpython.com/python-redis/

## Exemplos Flask + Redis

https://gist.github.com/swdevbali/f4adcacd402216256dd8

https://realpython.com/flask-by-example-implementing-a-redis-task-queue/

https://gist.github.com/calderonroberto/f4d8badb94c01e9020db

https://www.scaleway.com/en/docs/how-to-install-flask-on-your-server/


## Base de exemplo de conceitos de fila

https://towardsdatascience.com/use-redis-queue-for-asynchronous-tasks-in-a-flask-app-d39f2a8c2667

https://github.com/bee-queue/bee-queue (Somente adicionar tarefa na fila / Não processar ela automaticamente)

### Bypassing workers

For testing purposes, you can enqueue jobs without delegating the actual execution to a worker (available since version 0.3.1). To do this, pass the is_async=False argument into the Queue constructor:

https://python-rq.org/docs/#bypassing-workers

## 0 - Virtual env python
```
virtualenv venv
source venv/bin/activate
```
## 1 - Instalar Redis [OK]
```
pip3 install redis==3.4.1 rq==1.2.2
pip3 freeze > requirements.txt
pip3 install Flask
pip3 install rq
pip3 install redis
```
## 2 - Startar [OK]
```
 redis-server
 Start the redis queue worker: rq worker
 Empty all redis queues: rq empty --all

```

## 3 - Consultar as mensagens em fila [Doing]

## 4 - Manipular mensagens existentes (Push, Pop, Count)

## 5 - Manipular mensagens existentes através de rotas

## 6 - Implementar conceito de fila [OK]
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
