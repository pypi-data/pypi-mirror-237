#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pyttsx3

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()