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

### Put
```
curl -d '{"name":"jhon", "age":"46"}' -H "Content-Type: application/json" -X PUT http://localhost:5000/users/1
```

### Delete
```
curl -H "Content-Type: application/json" -X DELETE http://localhost:5000/users/1
```

## Product requests

### Get
```
curl -X GET http://localhost:5000/products
```

### Post
```
curl -d '{"name":"lollipop", "price":"2.7"}' -H "Content-Type: application/json" -X POST http://localhost:5000/products
```

### Put
```
curl -d '{"name":"lollipop", "price":"2.9"}' -H "Content-Type: application/json" -X PUT http://localhost:5000/products/1
```

### Delete
```
curl -H "Content-Type: application/json" -X DELETE http://localhost:5000/products/1
```

## Order requests

### Get
```
curl -X GET http://localhost:5000/orders
```

### Post
```
curl -d '{"userId":"1", "productId":"1"}' -H "Content-Type: application/json" -X POST http://localhost:5000/orders
```