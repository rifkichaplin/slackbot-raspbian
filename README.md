# slackbot-raspbian

```How to Install on Raspbian OS```
- sudo apt-get update
- sudo apt-get install python3
- sudo apt-get install python3-pip
- sudo apt-get install virtualenv
- sudo apt-get install gcc libffi-dev libssl-dev python-dev libpcap0.8-dev
- sudo pip3 install cryptography==2.0.1
- sudo pip3 install ansible==2.3.2
- ssh-keygen
- cp ~/.ssh/id_rsa.pub  ~/.ssh/authorized_keys
- chmod 600 ~/.ssh/authorized_keys
- ssh pi@localhost (check your ssh localhost connection without asking password)
