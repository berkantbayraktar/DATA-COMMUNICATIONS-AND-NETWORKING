#!/bin/bash

#directory = "/home/ilker/Desktop/courses/435\ -\ network/tp-part1/ceng435--term-project/"
#hostname = "pc3.instageni.rnet.missouri.edu:"
#user = "e2098770"
#target = "/users/e2098770"


eval `ssh-agent -s`
ssh-add ~/.ssh/id_geni_ssh_rsa 

scp -P 25571 /home/ilker/Desktop/courses/435\ -\ network/tp-part1/ceng435--term-project/destination.py e2098770@pc3.instageni.rnet.missouri.edu:/users/e2098770
scp -P 25572 /home/ilker/Desktop/courses/435\ -\ network/tp-part1/ceng435--term-project/r1.py e2098770@pc3.instageni.rnet.missouri.edu:/users/e2098770
scp -P 25573 /home/ilker/Desktop/courses/435\ -\ network/tp-part1/ceng435--term-project/r2.py e2098770@pc3.instageni.rnet.missouri.edu:/users/e2098770
scp -P 25570 /home/ilker/Desktop/courses/435\ -\ network/tp-part1/ceng435--term-project/broker.py e2098770@pc3.instageni.rnet.missouri.edu:/users/e2098770
scp -P 25574 /home/ilker/Desktop/courses/435\ -\ network/tp-part1/ceng435--term-project/source.py e2098770@pc3.instageni.rnet.missouri.edu:/users/e2098770