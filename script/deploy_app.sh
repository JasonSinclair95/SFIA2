#!/bin/bash
. ~/.bashrc
 
docker-compose build
 
docker push jasonsinclair95/sfia2:service1
 
docker push jasonsinclair95/sfia2:service2
 
docker push jasonsinclair95/sfia2:service3
 
docker push jasonsinclair95/sfia2:service4

docker stack deploy --compose-file docker-compose.yaml sfia2