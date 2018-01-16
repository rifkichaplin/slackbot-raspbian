import re
import requests
from subprocess import call, PIPE, Popen
import os
import jenkins
import random
import socket
from urllib.parse import urlparse
import sys

jenkinsurl=os.environ["SLACK_JENKINS_URL"] 
jenkinsusername=os.environ["SLACK_JENKINS_USERNAME"]
jenkinspassword=os.environ["SLACK_JENKINS_PASSWORD"]
server=jenkins.Jenkins(jenkinsurl, username=jenkinsusername, password=jenkinspassword, timeout=10)


def conn_jenkins():
    try:
        jenkinsurl_parse=urlparse(jenkinsurl)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.connect((jenkinsurl_parse.hostname, jenkinsurl_parse.port))
    except socket.error as e:
        return("Sorry, I can't serving you boss.. Jenkins {}".format(e))


def get_version_jenkins():
    try:
        version = server.get_version()
        return ("Your Jenkins version is {}".format(version))
    except Exception:
        return conn_jenkins()

       
def build_job_jenkins(job_name_par):
    try:
        job_name = job_name_par.replace(" ","")
        server.build_job(job_name, parameters=None, token="thisistokenjenkins")    
        return "Build job {} being process, please wait..".format(job_name)
    except Exception:
        return conn_jenkins()


def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]


def on_message(msg, server):
    text = msg.get("text", "")

    conversation = [
      "Please check jenkins version",
      "Jenkins version"
    ]
    for str in conversation:
        match = re.findall(r"{}( .*)?".format(str), text, flags=re.IGNORECASE)
        if match:
            return get_version_jenkins()


    conversation = [
      "Please deploy job",
      "Please build job",
      "Run job",
      "Please run job"
    ]
    for str in conversation:
        match = re.findall(r"{}( .*)?".format(str), text, flags=re.IGNORECASE)
        if match:
            return build_job_jenkins(match[0])


on_bot_message = on_message
