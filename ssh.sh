#!/bin/bash
#hostname = "pc3.instageni.rnet.missouri.edu"
#user = "e2098770"

eval `ssh-agent -s`
ssh-add ~/.ssh/id_geni_ssh_rsa 

ssh e2098770@pc3.instageni.rnet.missouri.edu -p 25571 # destination
ssh e2098770@pc3.instageni.rnet.missouri.edu -p 25573 # router2
ssh e2098770@pc3.instageni.rnet.missouri.edu -p 25572 # router1
ssh e2098770@pc3.instageni.rnet.missouri.edu -p 25570 # broker
ssh e2098770@pc3.instageni.rnet.missouri.edu -p 25574 # source