# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 21:15:50 2022

@author: Cayse Rogers
"""
import PySimpleGUI as sg
import PIL as pl
from PIL import ImageTk
import speech_recognition as sr





#sg.theme_previewer()
sg.theme('Tan')
bar = True


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()


#create and run alarms window
def Alarms():

    column = [[sg.Text("Alarm Functionality WIP",text_color = "orange",
                      justification="c",font =("Courier", 25),pad = (10,10))],
              [sg.Button("Back",size = (20,2),pad = (10,10))]]

    layout = [[sg.VPush()],
              [sg.Column(column,element_justification="c",justification="c",)],
              [sg.VPush()]]

    # Create and listen to window
    window = sg.Window("Alarms Test",layout,no_titlebar=bar,modal = True).Finalize()
    window.Maximize()
    choice = None
    while True:
        event, values = window.read()
        if event == "Back" or event == sg.WIN_CLOSED:
            break

    window.close()

# Create and run games window
def Games():
    column = [[sg.Text("No games at the moment. Sorry.",text_color = "orange",
                      justification="c",font =("Courier", 25),pad = (10,10))],
              [sg.Button("Back",size = (20,2),pad = (10,10))]]

    layout = [[sg.VPush()],
              [sg.Column(column,element_justification="c",justification="c",)],
              [sg.VPush()]]

    # Create and listen to window
    window = sg.Window("Games Test",layout,no_titlebar=bar,modal = True).Finalize()
    window.Maximize()
    choice = None
    while True:
        event, values = window.read()
        if event == "Back" or event == sg.WIN_CLOSED:
            break

    window.close()

# create and run main window
def main():
    WAKE_WORD = "hey Fred"
    logo = "logo2.png"
    # Resizing image for proper display
    im = pl.Image.open(logo)
    r = sr.Recognizer()
    if logo == "logo.png":
        imsize = (300,300)
    elif logo == "logo2.png":
        imsize = (300,150)
    im = im.resize(size = imsize, resample=pl.Image.BICUBIC)

    # Buttons and logo
    column = [[sg.Text("Hello. I am FRED.",
                       text_color = "orange",justification="c",
                       font =("Courier", 25),pad = (10,10))],
              [sg.Image(size=(300,300),key = "LOGO")],
              [sg.Button("Alarms",size = (20,2),pad = (10,10))],
              [sg.Button("Games",size = (20,2),pad = (10,10))],
              [sg.Button("Turn Off",size = (20,2),pad = (10,10))]]

    layout = [[sg.VPush()],
              [sg.Column(column,element_justification="c",justification="c",)],
              [sg.VPush()]]

    window = sg.Window("FRED Test",layout,no_titlebar=bar).Finalize()

    # Display image
    image = ImageTk.PhotoImage(image=im)
    window["LOGO"].update(data=image)

    window.Maximize()


    while True:

        text = get_audio()
        #sg.Text("Recognizing Now .... ")
        event, values = window.read()
        if event == "Turn Off" or event == sg.WIN_CLOSED:
            break
        elif event == "Alarms":
            Alarms()
        elif event == "Games":
            Games()




    window.close()

if __name__ == "__main__":
    main()
