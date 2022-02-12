# gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate's text-to-speech API.


import playsound as playsound
from gtts import gTTS
from playsound import playsound
from tkinter import *
import os
# The OS module in Python provides functions for interacting with the operating system

root = Tk()
root.configure(bg='ghost white')
root.title("Sumit - TEXT TO SPEECH")
root.geometry("350x300")

Label(root, text = "TEXT TO SPEECH", font = "arial 20 bold", bg='white smoke').pack()
Label(text ="© Owned by Sumit", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')
Msg = StringVar()
Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)
entry_field = Entry(root, textvariable = Msg ,width ='50')
entry_field.place(x=20,y=100)

def texttospeech():
    message = entry_field.get()
    speech = gTTS(text = message)
    speech.save('DataFlair.mp3')
    playsound('DataFlair.mp3')
    os.remove('DataFlair.mp3')

def exit():
    root.destroy()
def reset():
    Msg.set("")

Button(root, text = "PLAY", font = 'arial 15 bold' , command = texttospeech ,width = '4',bg = 'Green').place(x=25,y=140)
Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = exit, bg = 'OrangeRed1').place(x=100 , y = 140)
Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = reset, bg = 'Yellow').place(x=175 , y = 140)

root.mainloop()