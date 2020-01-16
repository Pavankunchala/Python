#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 19:24:30 2020

@author: pavankunchala
"""


from gtts import gTTS
import os
import webbrowser
import smtplib
import speech_recognition as sr


def talkToMe(audio):
    print(audio)
    tts =gTTS(text = audio,lang = 'en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')
    
    
#listen for commands
def myCommand():
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("I am ready for your next command Amigo")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source,duration = 1)
        audio = r.listen(source)
        
    try:
        command = r.recognize_google(audio)
        print('You said' + command + '/n')
        
    #loop for continuing to listen ur commands
    except sr.UnknownValueError:
        assistant(myCommand)
        
    return command

# statements for executing the commands
def assistant(command):
    
    if   'open Facebook' == command:
        chrome_path = '/Applications/Google Chrome.app'
        url ='https://www.facebook.com'
        webbrowser.get(chrome_path).open(url)
        
        
    if 'what \s up' == command:
        talkToMe('chillin bro')
        
    
    if 'how are you' == command:
        talkToMe('I am doing great')
        
    if 'open Youtube' == command:
        chrome_path = '/Applications/Google Chrome.app'
        url ='https://www.youtube.com'
        webbrowser.get(chrome_path).open(url)
        
        
        
talkToMe('I am ready for your command')


while True:
    assistant(myCommand)
        
        

        
        
        
        
        
        
        