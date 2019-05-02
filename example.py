from responsive_voice import ResponsiveVoice

engine = ResponsiveVoice()
engine.say("hello world")
engine.say("hello world",
           gender=ResponsiveVoice.MALE,
           lang=ResponsiveVoice.ENGLISH_GB,
           rate=0.4)

file_path = engine.get_mp3("ola mundo", lang=ResponsiveVoice.PORTUGESE_BR)
engine.play_mp3(file_path)
