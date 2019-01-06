FROM alpine:latest
MAINTAINER Ramesh Balaji "post2rb@hotmail.com"

# Flim docker image

# In order for the database to work: you MUST set the following environment variables when you run the image:
# FLIM_DB_NAME
# FLIM_DB_HOST
# FLIM_DB_PORT
# FLIM_DB_PROVIDER
# FLIM_DB_USERNAME
# FLIM_DB_PASSWORD

# Furthermore, you can set the following configuration variables

# FLIM_ALLOW_REGISTRATION (can be either 0 or 1, True or False)
# FLIM_HOST (IP Address Flim runs on)
# FLIM_PORT (Port Flim runs on)


# I think you can figure out what all of the environment variables mean, if you cannot, you are probably not qualified enough to set this system up.


ADD . /flim
WORKDIR /flim

RUN apk update
RUN apk upgrade
RUN apk add python3 python3-dev mariadb-connector-c-dev mariadb-client build-base linux-headers

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["wsgi.py"]


