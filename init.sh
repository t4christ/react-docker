#!/bin/bash
sudo yum update -y
sudo yum -y install docker
service docker start
usermod -a -G docker ec2-user
chkconfig docker on
pip3 install docker-compose 