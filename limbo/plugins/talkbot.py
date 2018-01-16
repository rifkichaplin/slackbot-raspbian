#!/usr/bin/env python
import re
import requests
from subprocess import call, PIPE, Popen
import os
import random

def cmdkill(command):
    process = Popen(
        args="pkill {}".format(command),
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]

def on_message(msg, server):
    text = msg.get("text", "")


    conversation = [
        "Hello",
        "Hi there",
        "where are you",
        "are you there"
    ]
    botanswer = [
        "Yes, I'm here boss.., Could I help you?",
        "Whats up boss.. Do you need a help?"
    ]
    for str in conversation:
        match = re.findall(r"{}( .*)?".format(str), text, flags=re.IGNORECASE)
        if match:
            return random.choice(botanswer)


    conversation = [
        "Awesome",
        "Great",
        "Cool",
        "Amazing"
    ]
    botanswer = [
        "Your welcome boss.. :)",
        "Same to you boss,."
    ]
    for str in conversation:
        match = re.findall(r"{}( .*)?".format(str), text, flags=re.IGNORECASE)
        if match:
            return random.choice(botanswer)


    conversation = [
        "Assalam",
        "Asalam",
    ]
    botanswer = [
        "Wa’alaikumus Salam my boss.. :)",
        "وعليكم سلام (And Peace Be Upon You Boss)"
    ]
    for str in conversation:
        match = re.findall(r"{}( .*)?".format(str), text, flags=re.IGNORECASE)
        if match:
            return random.choice(botanswer)

    
    conversation = [
        "Would you kill",
        "I need you to kill",
        "I need you kill"
        "Please kill"
    ] 
    botanswer = [
        "What you want boss, Already killed ",
        "You are so cruel boss, Already killed "
    ]
    for str in conversation:
        match = re.findall(r"{}( .*)?".format(str), text, flags=re.IGNORECASE)
        if match:
            cmdkill(match[0])
            return random.choice(botanswer)


    if not match:
       return

on_bot_message = on_message
