FROM python:3.9-slim-buster

EXPOSE 5000/tcp

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD ["src/app.py"]