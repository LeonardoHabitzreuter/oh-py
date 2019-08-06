# oh-py
Practicing some python

## Running the server
env FLASK_APP=server.py flask run

## Debugging
export FLASK_ENV=development

## User requests

### Get
```
curl -X GET http://localhost:5000/users
```

### Post
```
curl -d '{"name":"jhon", "age":"45"}' -H "Content-Type: application/json" -X POST http://localhost:5000/users
```

### Delete
```
curl -H "Content-Type: application/json" -X DELETE http://localhost:5000/users/1
```