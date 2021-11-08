from responsive_voice import ResponsiveVoice

engine = ResponsiveVoice()
engine.default_play_cmd = "mpg123 -o pulse -q %1"
engine.say("hello world")
engine.say("hello world",
           gender=ResponsiveVoice.MALE,
           rate=0.45)

engine = ResponsiveVoice(lang=ResponsiveVoice.PORTUGUESE_BR)
file_path = engine.get_mp3("olá mundo")
engine.play_mp3(file_path)

from responsive_voice.voices import EnglishIndia, UKEnglishMale, \
    PortuguesePortugal

india = EnglishIndia()
uk = UKEnglishMale()
pt = PortuguesePortugal()
india.say("hello world")
uk.say("hello world")
pt.say("olá mundo")
