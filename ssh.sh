#!/bin/bash

host = pc3.instageni.rnet.missouri.edu
user = e2098770

eval `ssh-agent -s`
ssh-add ~/.ssh/id_geni_ssh_rsa 

ssh ${user}@${host} -p 25571 # destination
ssh ${user}@${host} -p 25573 # router2
ssh ${user}@${host} -p 25572 # router1
ssh ${user}@${host} -p 25570 # broker
ssh ${user}@${host} -p 25574 # source