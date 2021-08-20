from subprocess import call
import os

class Actions:
    def __init__(self):
        print("Inited Actions")

    def volume(self, value):
        if type(value) == int:
            print(f"Volume {value}")
            call(["/var/run/host/usr/bin/amixer", "-D", "pulse", "sset", "Master", str(value)+"%"])



    def mute(self, value):
        if value != False:
            print("Mute")
            call(["/var/run/host/usr/bin/amixer", "-D", "pulse", "sset", "Master", "mute"])

    def unmute(self, value):
        if value != False:
            print("UnMute")
            call(["/var/run/host/usr/bin/amixer", "-D", "pulse", "sset", "Master", "unmute"])

    def play(self, value):
        if value != False:
            print("Play")
            call(["/var/run/host/usr/bin/xdotool", "key", "XF86AudioPlay"])

    def pause(self, value):
        if value != False:
            print("pause")
            call(["/var/run/host/usr/bin/xdotool", "key", "XF86AudioPause"])

    def next(self, value):
        if value != False:
            print("next")
            call(["/var/run/host/usr/bin/xdotool", "key", "XF86AudioNext"])

    def prev(self, value):
        if value != False:
            print("prev")
            call(["/var/run/host/usr/bin/xdotool", "key", "XF86AudioPrev"])
