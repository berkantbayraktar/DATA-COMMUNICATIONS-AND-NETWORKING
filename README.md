İlker Ayçiçek - 2098770

Berkant Bayraktar- 2098796


We have 5 different python files. Namely,

* destination.py
* r1.py
* r2.py
* broker.py
* source.py

Each of them is  uploaded different vm machines with respect to their name.
(i.e. destination into vm machine `d` etc.)

First , we run ssh-agent to add ssh public key :
```
    eval `ssh-agent -s`
    ssh-add ~/.ssh/id_geni_ssh_rsa 
```
After these commands, we enter our passphrase. Then use scp to upload files 
to remote virtual machines by :

```
    scp -P <port-number-of-the-machine> <path-to-your-file> berkantb@pc5.instageni.rnet.missouri.edu
    :/users/berkantb
```

* path-to-your-file: directory of the file that you want to copy
* host : target hostname {e.g. pc5.instageni.rnet.missouri.edu}
* user : GENI username (e.g. berkantb)

After we upload our files to each machine, we connect to machines via ssh.

```
   ssh -i <path-to-your-private-key-file> berkantb@pc5.instageni.rnet.missouri.edu
    -p <port-number-of-the-machine>
```
* path-to-your-private-key-file : directory of the private key for GENI 
* host : target hostname {e.g. pc5.instageni.rnet.missouri.edu}
* user : GENI username (e.g. berkantb)


We connected to machines.Then, for time syncronization between
machines we use ntp on source and destination machines:

```
sudo service ntp stop
sudo ntpdate 1.ro.pool.ntp.org

```
We checked if it is syncronized or not by :
```
timedatectl status
```
You don't need to synchronize again. We already did.It is enough to
do it once. After synchronizing,we ran our socket programs on each machine:
```
    python destination.py
    python r1.py
    python r2.py
    python broker.py
    python source.py
```

In our `source.py`, we take input from our predefined file. It automatically,
parses file into chunks and send them one by one. You can find end-to-end delay
of each packets and average end-to-end delay of these packets, 
in the standard output of `source` node.

After finding correct internet interfaces of nodes by ```ifconfig``` command,

For experiment 1:

* We added 1ms+-5ms network emulating delay to the eth0 and eth1 interface 
    for r1 and r2 links of destination node.

* For r1 link :
```
    sudo tc qdisc add dev eth2 root netem delay 1ms 5ms distribution normal
```
* For r2 link:
```
    sudo tc qdisc add dev eth1 root netem delay 1ms 5ms distribution normal
```
 

* We added 1ms+-5ms network emulating delay to the eth0 and eth1 interface 
    for r1 and r2 links of broker node.

* For r1 link :
```
    sudo tc qdisc add dev eth1 root netem delay 1ms 5ms distribution normal
```
* For r2 link:
```
    sudo tc qdisc add dev eth1 root netem delay 1ms 5ms distribution normal
```

For experiment 2:

* We changed to 20ms+-5ms network emulating delay to the eth0 and eth1 interface 
    for r1 and r2 links of destination node.

* For r1 link :
```
    sudo tc qdisc change dev eth2 root netem delay 20ms 5ms distribution normal
```
* For r2 link:
```
    sudo tc qdisc change dev eth1 root netem delay 20ms 5ms distribution normal
```
 

* We changed to 20ms+-5ms network emulating delay to the eth0 and eth1 interface 
    for r1 and r2 links of broker node.

* For r1 link :
```
    sudo tc qdisc change dev eth1 root netem delay 20ms 5ms distribution normal
```
* For r2 link:
```
    sudo tc qdisc change dev eth1 root netem delay 20ms 5ms distribution normal
```

For experiment 3:

* We changed to 60ms+-5ms network emulating delay to the eth0 and eth1 interface 
    for r1 and r2 links of destination node.

* For r1 link :
```
    sudo tc qdisc change dev eth2 root netem delay 60ms 5ms distribution normal
```
* For r2 link:
```
    sudo tc qdisc change dev eth1 root netem delay 60ms 5ms distribution normal
```
 

* We changed to 60ms+-5ms network emulating delay to the eth0 and eth1 interface 
    for r1 and r2 links of broker node.

* For r1 link :
```
    sudo tc qdisc change dev eth1 root netem delay 60ms 5ms distribution normal
```
* For r2 link:
```
    sudo tc qdisc change dev eth1 root netem delay 60ms 5ms distribution normal
```
___

Then, for each experiment we calculated average end-to-end delay for 154 packets
for each  epxeriment.