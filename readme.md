## Python Responsive Voice

Unofficial python API for [Responsive Voice](https://responsivevoice.org)

## install

    pip install responsivevoice

## usage

    from responsive_voice import ResponsiveVoice

    engine = ResponsiveVoice()
    engine.say("hello world")

    engine = ResponsiveVoice(rate=0.4, vol=0.8)

    engine.say("hello world", gender="male", lang="en-GB")

    file_path = engine.get_mp3(u"ola mundo", lang="pt-pt")

    engine.play_mp3(file_path)

## credits

JarbasAI
