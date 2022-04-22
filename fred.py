# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 21:15:50 2022

@authors: Cayse Rogers
"""

import PySimpleGUI as sg
import PIL as pl
from PIL import ImageTk
from datetime import datetime
from playsound import playsound
import time
from pygame import mixer
import threading
import speech_recognition as sr
import pyttsx3
import subprocess
import pyjokes



WAKE_WORD = "hey Fred"
r = sr.Recognizer()

bar = False
font = "Gotham"
orange = "#FF8200"
grey = "#58595B"

# Default colors
sg.theme_background_color(grey)
sg.theme_element_background_color(grey)
sg.theme_text_element_background_color(grey)
sg.theme_element_text_color(orange)
sg.theme_input_text_color(orange)
sg.theme_text_color(orange)
hours_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
min_list = [str(val).zfill(2) for val in range(60)]

# get audio used for voice assistant
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print("you said " + said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()

# text-to-speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# note taking
def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


# create and run alarms window
def Alarms():
    bar = True
    column = [[sg.Text("Alarm Functionality WIP",
                       justification="c", font=(font, 25), pad=(10, 10))],
              [sg.Button("Back", size=(20, 2), pad=(10, 10))]]
    c_temp = [[sg.Text("Enter Hour (HH):")],
              [sg.OptionMenu(values=hours_list, default_value="12")],
              [sg.Text("Enter Minute (MM):")],
              [sg.OptionMenu(values=min_list, default_value="00")],
              [sg.Text("Enter Period (AM/PM):")],
              [sg.OptionMenu(values=["AM", "PM"], default_value="PM")],
              [sg.Submit(), sg.Cancel()]]
    lay_temp = [[sg.VPush()],
                [sg.Column(c_temp, element_justification="c", justification="c")],
                [sg.VPush()]]
    layout = [[sg.VPush()],
              [sg.Column(column, element_justification="c", justification="c")],
              [sg.VPush()]]
    win_temp = sg.Window("Input Alarm Values", lay_temp, no_titlebar=bar, modal=True).Finalize()
    while True:
        event, values = win_temp.read()
        hour = values[0].strip()
        a_min = values[1].strip()
        period = values[2].strip()
        # a_min = values[1].strip()
        # period = values[2].strip()
        if int(hour) <= 12 and int(a_min) <= 59 and (period == "AM" or period == "PM"):
            # win_temp.close()
            print("good")
            break
    print(hour)
    print(period)
    print(a_min)
    '''
    while True:
        now = datetime.now()

        current_hour = now.strftime("%I")
        current_min = now.strftime("%M")
        current_period = now.strftime("%p")
        current_sec = now.strftime("%S")
        if period == current_period:
            if hour == current_hour:
                if a_min == current_min:
                    if "00" == current_sec:
                        print("Wake Up!")
                        mixer.init()
                        mixer.music.load("loud_alarm_clock.mp3")
                        mixer.music.play()
                        while mixer.music.get_busy():
                            time.sleep(1)
                        break
    '''
    win_temp.close()

    # Create and listen to window
    window = sg.Window("Alarms Test", layout, no_titlebar=bar, modal=True).Finalize()
    window.Maximize()

    while True:
        event, values = window.read(timeout=1)

        now = datetime.now()

        current_hour = now.strftime("%I")
        current_min = now.strftime("%M")
        current_period = now.strftime("%p")
        """
        print(hour)
        print(period)
        print(a_min)
        """
        if period == current_period:
            if hour == current_hour:
                if a_min == current_min:
                    mixer.init()
                    mixer.music.load("loud_alarm_clock.mp3")
                    mixer.music.play()
                    while mixer.music.get_busy():
                        time.sleep(1)
                        break

        if event == "Back" or event == sg.WIN_CLOSED:
            break

    window.close()


# Create and run games window
def Games():
    column = [[sg.Text("No games at the moment. Sorry.",
                       justification="c", font=(font, 25), pad=(10, 10))],
              [sg.Button("Back", size=(20, 2), pad=(10, 10))]]

    layout = [[sg.VPush()],
              [sg.Column(column, element_justification="c", justification="c")],
              [sg.VPush()]]

    # Create and listen to window
    window = sg.Window("Games Test", layout, no_titlebar=bar, modal=True).Finalize()
    window.Maximize()
    while True:
        event, values = window.read()
        if event == "Back" or event == sg.WIN_CLOSED:
            break

    window.close()


# create and run main window
def main():
    logo = "logo2.png"
    # Resizing image for proper display
    im = pl.Image.open(logo)
    if logo == "logo.png":
        imsize = (300, 300)
    elif logo == "logo2.png":
        imsize = (300, 150)
    im = im.resize(size=imsize, resample=pl.Image.BICUBIC)
    '''
    alarm_thread = threading.Thread(target=Alarms)
    alarm_thread.start()
    '''
    # Buttons and logo
    column = [[sg.Text("Hello. I am FRED.", justification="c",
                       font=(font, 25), pad=(10, 10))],
              [sg.Image(size=(300, 300), key="LOGO")],
              [sg.Button("Alarms", size=(20, 2), pad=(10, 10))],
              [sg.Button("Games", size=(20, 2), pad=(10, 10))],
              [sg.Button("Turn Off", size=(20, 2), pad=(10, 10))]]

    layout = [[sg.VPush()],
              [sg.Column(column, element_justification="c", justification="c")],
              [sg.VPush()]]

    window = sg.Window("FRED Test", layout, no_titlebar=bar).Finalize()

    # Display image
    image = ImageTk.PhotoImage(image=im)
    window["LOGO"].update(data=image)

    window.Maximize()

    while True:
        event, values = window.read(timeout = 1)
        if event == "Turn Off" or event == sg.WIN_CLOSED:
            break
        elif event == "Alarms":
            Alarms()
        elif event == "Games":
            Games()

    window.close()


if __name__ == "__main__":
    main()
