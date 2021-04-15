# api.limon.sh

[![Deploy to Amazon ECS](https://github.com/limon-sh/api.limon.sh/actions/workflows/aws.yml/badge.svg)](https://github.com/limon-sh/api.limon.sh/actions/workflows/aws.yml)

The project follows the style described in [pep8](https://www.python.org/dev/peps/pep-0008/)

### Build

After build service is available on [http://0.0.0.0:8082](http://0.0.0.0:8082)

```bash
$ docker-compose up --build
```

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
$ docker-compose run backend pytest tests
```


### Linters

Run linter:

```bash
$ docker-compose run backend flake8 apps
```
