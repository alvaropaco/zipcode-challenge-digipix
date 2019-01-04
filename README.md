### Digipix Consulta CEP

O Objetivo deste projet e realizar a consulta atraves da API da Digipix a um CEP requisitado.

# Requisitos

* Docker I/O

# Intrduç~ao

Este serviço foi implementado em um contexto de arquitetura de Software de microserviços em Python.  'E constituido de um servidor Flask para rotear as chamadas de API, um message broker RabbitMQ, e um mirco serviço em Nameko.

# Build

`docker build -t digipix . `

# Uso

> voc^e deve exportar uma vari'avel JWT com o valor do seu token de autorizaç~ao

`docker run -it -v $(d):/app -e JWT=$(echo $JWT) -p 5000:5000 digipix` 

O serviço ser'a exposto na porta 5000 da m'aquina loca. Voc^e pode consultar o endpoint do a chamada:

`curl -X GET 127.0.0.1:5000/zipcode?code=13560044`
