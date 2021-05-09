# Simple blog management Rest API in Python using Fast API

A small example to get acquainted with the framework, no frontend and no real database, just storing data in the memory.

Main functions:

* Creating a new blog post
* Editing blog post
* Deleting blog post
* List blog post
* View blog post detail


## Requirements


`sudo dnf install podman` or [Install Docker Engine](https://docs.docker.com/install/).

`sudo dnf install podman-compose` or [Install Docker Compose](https://github.com/docker/compose/releases/latest).

`sudo dnf install git` or [Install git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).


## Build
Please note this is example development build.

```bash
git clone https://github.com/spital/fastapi-test-blog
cd fastapi-test-blog
podman-compose build
```

## Source tests
*TODO*: pylint, unittest, sonarqube, ...


## Run

```bash
podman-compose up -d
podman-compose logs -f web
```

## Api test

```bash
podman exec -it fastapi-test-blog_web_1 sh -c 'pytest /usr/src/app'
```

## Use
Start web browser and go to (http://localhost:8002/) for API root

or (http://localhost:8002/redoc) for API docs

or (http://localhost:8002/docs) for API docs with tryouts.

