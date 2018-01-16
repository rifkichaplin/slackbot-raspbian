# slackbot-raspbian
### A [Slack](https://slack.com/) chatbot modify based on code [llimlib](https://github.com/llimllib/limbo), Thanks to llimllib

## Installation Ansible 2.3 on Raspbian OS
* sudo apt-get update
* sudo apt-get install python3
* sudo apt-get install python3-pip
* sudo apt-get install virtualenv
* sudo apt-get install gcc libffi-dev libssl-dev python-dev libpcap0.8-dev
* sudo pip3 install cryptography==2.0.1
* sudo pip3 install ansible==2.3.2
* ssh-keygen
* cp ~/.ssh/id_rsa.pub  ~/.ssh/authorized_keys
* chmod 600 ~/.ssh/authorized_keys
* ssh pi@localhost (check your ssh localhost connection without asking password)

## Installation Slackbot Raspbian 
* virtualenv ~/env_slackbot_raspbian
* source ~/env_slackbot_raspbian/bin/activate
* Clone the repo
* [Create a bot user](https://my.slack.com/services/new/bot) if you don't have one yet, and copy the API Token
* export SLACK_TOKEN="your-api-token"
* export SLACK_JENKINS_URL="http://{your-jenkins-ip}:{your-jenkins-port}"
* export SLACK_JENKINS_USERNAME="jenkins-username"
* export SLACK_JENKINS_PASSWORD="jenkins-password"
* make clean
* make install
* make run
* start to chat your bot with says  "Hello"
