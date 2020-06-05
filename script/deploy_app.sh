#!/bin/bash
sudo source ~/.bashrc
sudo sudo docker-compose down 
sudo sleep 5
sudo docker-compose up --build -d
sudo sleep 15