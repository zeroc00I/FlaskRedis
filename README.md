# Chall

// Instalar Redis
// https://dev.to/divshekhar/how-to-use-redis-with-python-1nd6
// https://realpython.com/python-redis/

// Exemplos Flask + Redis
// https://gist.github.com/swdevbali/f4adcacd402216256dd8
// https://realpython.com/flask-by-example-implementing-a-redis-task-queue/
// https://gist.github.com/calderonroberto/f4d8badb94c01e9020db
// https://www.scaleway.com/en/docs/how-to-install-flask-on-your-server/

// Mais completo com conceito de fila
// https://towardsdatascience.com/use-redis-queue-for-asynchronous-tasks-in-a-flask-app-d39f2a8c2667

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

## 3 - Popular com novas mensagens [OK]

## 4 - Conseguir consultas as mensagens [OK]

## 5 - Manipular mensagens existentes (Push, Pop, Count)

## 6 - Manipular mensagens existentes através de rotas

## 7 - Implementar conceito de fila [OK]

curl -X POST http://127.0.0.1:5000/enqueue -d '{"hello":"world"}'
{
  "job_id": "4dfd1d5b-cf3b-4366-83a8-afa4f5de5244"
}

http://127.0.0.1:5000/get_result?job_id=4dfd1d5b-cf3b-4366-83a8-afa4f5de5244

{
  "input": null, 
  "job_enqueued_at": "2021-01-14T00:55:23.500216", 
  "job_id": "4dfd1d5b-cf3b-4366-83a8-afa4f5de5244", 
  "job_started_at": "2021-01-14T00:57:42.565441", 
  "result": null
}
