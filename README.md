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

You can run our  script `transfer_files.sh` to upload files to vm machines.

```
    sh transfer_files.sh
```
This script uses scp to upload files. It first runs `ssh-agent` to simplify
public key process and asks your passphrase.After passphrase is entered, it 
copies corresponding files to target vm.

You can change the vm addresses, target directory and local directory easily
in the script file.

* directory : directory of the file that you want to copy (e.g. ~/Desktop)
* host : target hostname {e.g. pc3.instageni.rnet.missouri.edu}
* user : username that is defined to you by the vm machine (e.g. e2098770)

After uploading files, you can connect to machines via 
`run_remote_files.sh` script.

```
    sh run_remote_files.sh
```
This script uses ssh for connection. It first runs `ssh-agent` to simplify
public key process and asks your passphrase. After passphrase is entered, it 
connects to machines in 5 different terminal screen.

You can change the ports of the machines that you want to connect by changing
25571 .. 25574 part of the for loop.

* host : hostname of the target machine
* user : username that is defined to you by the vm machine (e.g. e2098770, berkantb etc.)

After connecting, you can run python executables on each different terminal
(vm machine).

```
    python destination.py
    python r1.py
    python r2.py
    python broker.py
    python source.py
```
We run our scripts and connected to machines. For time syncronization between
machines we use ntp on each individual machine:

```
sudo service ntp stop
sudo ntpdate 1.ro.pool.ntp.org

```

In our `source.py`, we take input from our predefined file. It automatically,
parses file into chunks and send them one by one. You can find end-to-end delay,
in the standard output of `source` node.

For adding/changing network emulating delays, following command adds 1ms+-5ms 
normal distribution network emulating delay to the eth0 interface.

```
    sudo tc qdisc change dev eth0 root netem delay 1ms 5ms distribution normal
```

You can find required interface name (e.g. eth0) to change emulate delay by:

```
    ifconfig
```

Find the IP that you are using while connecting through your socket to vm. 
Interface name of the corresponding IP is what you need.
We used following commands to emulate delays:

* For router1-----destination link. In destination machine, run:
    * To change :
```
    sudo tc qdisc change dev eth2 root netem delay 1ms 5ms distribution normal
    sudo tc qdisc change dev eth2 root netem delay 20ms 5ms distribution normal
    sudo tc qdisc change dev eth2 root netem delay 60ms 5ms distribution normal
```

    * To add :

```
    sudo tc qdisc add dev eth2 root netem delay 1ms 5ms distribution normal
    sudo tc qdisc add dev eth2 root netem delay 20ms 5ms distribution normal
    sudo tc qdisc add dev eth2 root netem delay 60ms 5ms distribution normal
```

 For router2----destination link. In destination machine, run:
   
    * To change :

```
    sudo tc qdisc change dev eth1 root netem delay 1ms 5ms distribution normal
    sudo tc qdisc change dev eth1 root netem delay 20ms 5ms distribution normal
    sudo tc qdisc change dev eth1 root netem delay 60ms 5ms distribution normal
```

    * To add:

```
    sudo tc qdisc add dev eth1 root netem delay 1ms 5ms distribution normal
    sudo tc qdisc add dev eth1 root netem delay 20ms 5ms distribution normal
    sudo tc qdisc add dev eth1 root netem delay 60ms 5ms distribution normal
```

 For router2----broker link In router2 machine, run:
  
    * To change :
```
    sudo tc qdisc change dev eth2 root netem delay 1ms 5ms distribution normal
    sudo tc qdisc change dev eth2 root netem delay 20ms 5ms distribution normal
    sudo tc qdisc change dev eth2 root netem delay 60ms 5ms distribution normal
```
 
    * To add:

```
    sudo tc qdisc add dev eth2 root netem delay 1ms 5ms distribution normal
    sudo tc qdisc add dev eth2 root netem delay 20ms 5ms distribution normal
    sudo tc qdisc add dev eth2 root netem delay 60ms 5ms distribution normal
```

 For router1----broker link. In router1 machine, run:
 
    * To change:

```
    sudo tc qdisc change dev eth1 root netem delay 1ms 5ms distribution normal
    sudo tc qdisc change dev eth1 root netem delay 20ms 5ms distribution normal
    sudo tc qdisc change dev eth1 root netem delay 60ms 5ms distribution normal
```

    * To add:

```
    sudo tc qdisc add dev eth1 root netem delay 1ms 5ms distribution normal
    sudo tc qdisc add dev eth1 root netem delay 20ms 5ms distribution normal
    sudo tc qdisc add dev eth1 root netem delay 60ms 5ms distribution normal
```

