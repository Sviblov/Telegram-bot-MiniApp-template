#!/bin/bash

sudo docker-compose -f /home/ubuntu/TG_Bot_Boilerplate/docker-compose.yml down

git -C /home/ubuntu/TG_Selflove_bot pull

#build react project

npm --prefix /home/ubuntu/G_Bot_Boilerplate/frontend run build



#up containers again

sudo docker-compose -f /home/ubuntu/TG_Bot_Boilerplate/docker-compose.yml up --build -d
