### Digipix Consulta CEP [![CircleCI](https://circleci.com/gh/alvaropaco/zipcode-challenge-digipix/tree/master.svg?style=svg)](https://circleci.com/gh/alvaropaco/zipcode-challenge-digipix/tree/master)

O Objetivo deste projet e realizar a consulta atraves da API da Digipix a um CEP requisitado.

# Requisitos

* Docker I/O

# Intrdução

Este serviço foi implementado em um contexto de arquitetura de Software de microserviços em Python. É constituido de um servidor Flask para rotear as chamadas de API, um message broker RabbitMQ, e um mirco serviço em Nameko.

# Build

`docker build -t digipix . `

# Uso

> Você deve exportar uma variável JWT com o valor do seu token de autorizaç~ao

`docker run -it -e JW$(echo $JWT) -p 5000:5000 digipix /app/entrypoint.sh` 

O serviço será exposto na porta 5000 da máquina loca. Você pode consultar o endpoint do a chamada:

`curl -X GET 127.0.0.1:5000/zipcode?code=13560044`


# Testing

`docker run -it -e JWT=$(echo $JWT) digipix /app/entrypoint.tests.sh`