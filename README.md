# Backend limon.sh

The project follows the style described in [pep8](https://www.python.org/dev/peps/pep-0008/)

### Build

After build service is available on [http://0.0.0.0:8081](http://0.0.0.0:8081)

```bash
$ docker-compose up --build
```
__

### Migrations

```bash
$ docker-compose run backend python3 manage.py makemigrations <APP_NAME>
```

### Tests

Base tests:

```bash
$ docker-compose run backend pytest tests
```

Test coverage:

```bash
$ docker-compose run backend pytest tests --cov=apps
```


### Linters

Run linter:

```bash
$ docker-compose run backend pylint --rcfile=tests/.pylintrc apps
```
