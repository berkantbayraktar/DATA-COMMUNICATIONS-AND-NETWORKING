#!/usr/bin/env bash

host=pc3.instageni.rnet.missouri.edu
user=e2098770



eval `ssh-agent -s`
ssh-add ~/.ssh/id_geni_ssh_rsa 
for port in 25571 25573 25572 25570 25574 
do
    gnome-terminal -x bash -c "ssh ${user}@${host} -p ${port} 'python *.py';exec bash" #destination
    sleep 1
done
