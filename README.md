# Questionarium Service

TODO: Describe project

## Running
```sh
. venv/bin/activate
flask run
```

```sh
docker run -it --rm --name postgres -p 5432:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=password -e POSTGRES_DB=questionarium -d postgres
docker run -it --rm --link postgres:db --name adminer -p 8080:8080 -d adminer
```

```sh
curl -X POST http://localhost:5000/questions -d '{ "title": "Question title", "answer": "Question answer", "category": "python" }' -H "Content-Type: application/json"
```

https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#quickstart
https://marshmallow.readthedocs.io/en/stable/examples.html#quotes-api-flask-sqlalchemy
https://realpython.com/flask-connexion-rest-api-part-2/
```sh
$ python
$ from app import db
$ db.create_all()
$ from app import Question
$ q = Question(title='question title', answer='question answer')
$ db.session.add(q)
$ db.session.commit()
$ Question.query.all()
```
