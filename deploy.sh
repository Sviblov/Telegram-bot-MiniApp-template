#!/bin/bash

sudo docker-compose -f /home/ubuntu/TG_Bot_Boilerplate/docker-compose.yml down

git -C /home/ubuntu/TG_Selflove_bot pull

#up containers again

sudo docker-compose -f /home/ubuntu/TG_Bot_Boilerplate/docker-compose.yml up --build -d
