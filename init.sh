#!/bin/bash
sudo yum update -y 
sudo yum -y install docker python3 python3-pip
sudo systemctl enable docker
sudo systemctl start docker
usermod -aG docker $USER && sudo newgrp docker && docker swarm init & \
# sudo docker network create --driver=bridge --attachable redis_nw
# sudo docker network create --driver=bridge --attachable web_nw
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
# sudo docker-compose up -d
pip3 install virtualenv

