#!/bin/bash
service rabbitmq-server start
nameko run zipcode &
python api.py runserver --host 0.0.0.0