#!/bin/bash

if [ "$1" = "test" ]
then
    docker-compose run --rm app sh -c 'python manage.py test && flake8'
elif [ "$1" = "startapp" ]
then
    docker-compose run --rm app sh -c "python manage.py startapp $2"
elif [ "$1" = "run" ]
then
    docker-compose up -d
elif [ "$1" = "down" ]
then
    docker-compose down
fi