"""
ADD APP/SCRIPT/MODULE TITLE

ADD SUMMARY OF APP/SCRIPT/MODULE HERE

------------------------------------------------------------------------------
Project:   ICT40220-IntroP4RIoT-Notes
Folder:    Session-13
Filename:  text-to-speach-1.py
Author:    Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
Version:   0.0
------------------------------------------------------------------------------
"""


import pyttsx3 #import the library

def voice_change():
    eng = pyttsx3.init() #initialize an instance
    voice = eng.getProperty('voices') #get the available voices
    print(voice)
    # eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
    # eng.setProperty('voice', voice[1].id) #changing voice to index 1 for female voice
    eng.say("This is a demonstration of how to convert index of voice using pyttsx3 library in python.") #say method for passing text to be spoken
    eng.runAndWait() #run and process the voice command
    eng.stop()

if __name__ == "__main__":
    voice_change()