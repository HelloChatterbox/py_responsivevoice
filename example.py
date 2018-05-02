from responsive_voice import ResponsiveVoice

engine = ResponsiveVoice()
engine.say("hello world")
engine.say("hello world", gender="male", lang="en-GB", rate=0.4)

file_path = engine.get_mp3(u"ola mundo", lang="pt-pt")
engine.play_mp3(file_path)
