# Flim
Flim is a lightweight forum written in Flask and Python3. 

## Hacking

To get started, you'll want the following:

* A Linux-based development environment (Debian or Fedora work best)
* MariaDB/MySQL with a user and database created for development
* Python 3.6 or later
* Python header libraries (libpython3-dev or python3-devel)
* MariaDB/MySQL header libraries (`libmysql-dev` or `mysql-devel`)

In order to install the dependencies required, run:

```bash
$ pip3 install --user -r requirements.txt
```

Now, you must populate the database. In order for flim to establish a connection to your database, you must copy the file `app/.flaskenv.example` to `app/.flaskenv` and edit the environment variables for the database to suit your development environment.

Next, **in the `app` directory**, run:

```bash
$ flask shell
```

In the shell, type:

```python
from app import db
db.create_all()
```

You can now start working on the application.

In the `app` directory, run:

```bash
$ flask run
```

