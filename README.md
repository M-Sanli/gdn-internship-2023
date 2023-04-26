# Backend oriented task (Java/Python/JS/.NET)

## How to use it

- To start the server, run this command:
```
python src/app.py
```
- To query operation 1, run this command (which should have the value 5.2768 as the returning information):
```
curl http://127.0.0.1:5000/exchanges/GBP/2023-01-02
```
- To query operation 2, run this command (which should have the values 5.1861 for min and 5.3648 for max as the returning information):
```
curl http://127.0.0.1:5000/max-min-average-value/gbp/20
```
- To query operation 3, run this command (which should have the value 0.107 as the returning information):
```
curl http://127.0.0.1:5000/major-difference-between-buy-ask/gbp/20
```

## Unit Tests

- To run unit tests:
```
pytest tests
```


## Run Dockerfile

- Firstly create the image on the same folder with Dockerfile:
```
docker image build -t api_server
```

- Secondly you can run the container for the image e created above. 
```
docker run -p 5000:5000 -d api_server
```
### Now, api_server  web api is ready on the localhost:5000



