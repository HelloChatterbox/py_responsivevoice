#!/usr/bin/python3

from responsive_voice import ResponsiveVoice

engine = ResponsiveVoice()
engine.say("hello world")

engine = ResponsiveVoice(rate=0.5, vol=1)

engine.say("hello world", gender=ResponsiveVoice.MALE, lang=ResponsiveVoice.ENGLISH_US)

file_path = engine.get_mp3(u"hola mundo", lang=ResponsiveVoice.PORTUGESE_PT)

engine.play_mp3(file_path)
