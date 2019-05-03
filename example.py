from responsive_voice import ResponsiveVoice

engine = ResponsiveVoice()
engine.say("hello world")
engine.say("hello world",
           gender=ResponsiveVoice.MALE,
           rate=0.45)

engine = ResponsiveVoice(lang=ResponsiveVoice.PORTUGUESE_BR)
file_path = engine.get_mp3(u"olá mundo")
engine.play_mp3(file_path)

from responsive_voice.voices import EnglishIndia, UKEnglishMale, \
    FallbackUKEnglishMale

india = EnglishIndia()
uk = UKEnglishMale()
uk2 = FallbackUKEnglishMale()
india.say("hello world")
uk.say("hello world")
uk2.say("hello world")
