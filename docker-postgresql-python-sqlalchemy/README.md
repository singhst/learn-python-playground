

How to Connect to mysql Docker from Python application on MacOS Mojave

https://medium.com/swlh/how-to-connect-to-mysql-docker-from-python-application-on-macos-mojave-32c7834e5afa


# PSQL

1. See running container ID
```shell
$ docker ps -l
CONTAINER ID   IMAGE                   COMMAND                  CREATED       STATUS             PORTS                    NAMES
e6ed0d2e95e4   bitnami/postgresql:12   "/opt/bitnami/script…"   8 weeks ago   Up About an hour   0.0.0.0:5432->5432/tcp   untitledfolder_postgresql12_1
```

2. Access the container by `CONTAINER ID`
```shell
$ docker exec -it e6ed0d2e95e4 /bin/sh
(inside container)$
```

3. Access the PostgreSQL db
```shell
# inside the running container
$ psql --username=<USERNAME> --password --host=<HOSTNAME> --port=<PORT>

$ psql --host=localhost --port=5432 --username=postgres --password
$ psql postgresql://postgres:pwd0123456789@localhost:5432/my_database
```