# api.limon.sh

[![Build Status](https://travis-ci.com/limon-sh/api.limon.sh.svg?branch=master)](https://travis-ci.com/limon-sh/api.limon.sh)
[![codecov](https://codecov.io/gh/limon-sh/api.limon.sh/branch/master/graph/badge.svg?token=DW71KUIRYO)](https://codecov.io/gh/limon-sh/api.limon.sh)

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
