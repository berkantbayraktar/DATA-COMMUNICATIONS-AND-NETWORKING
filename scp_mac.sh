#!/bin/bash

directory= ~/Desktop/ceng435/ceng435--term-project/
host=pc3.instageni.rnet.missouri.edu
user=berkantb


eval `ssh-agent -s`
ssh-add ~/.ssh/id_geni_ssh_rsa

scp -P 25571 ${directory}'destination.py' ${user}@${host}':/users/'${user}
scp -P 25572 ${directory}'r1.py' ${user}@${host}':/users/'${user}
scp -P 25573 ${directory}'r2.py' ${user}@${host}':/users/'${user}
scp -P 25570 ${directory}'broker.py' ${user}@${host}':/users/'${user}
scp -P 25574 ${directory}'source.py' ${user}@${host}':/users/'${user}
