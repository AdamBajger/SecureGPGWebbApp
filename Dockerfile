FROM python:3.13.2-alpine


# Set the working directory in the container
WORKDIR /app

RUN pdm install

