## Python Responsive Voice
[![Donate with Bitcoin](https://en.cryptobadges.io/badge/micro/1QJNhKM8tVv62XSUrST2vnaMXh5ADSyYP8)](https://en.cryptobadges.io/donate/1QJNhKM8tVv62XSUrST2vnaMXh5ADSyYP8)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://paypal.me/jarbasai)
<span class="badge-patreon"><a href="https://www.patreon.com/jarbasAI" title="Donate to this project using Patreon"><img src="https://img.shields.io/badge/patreon-donate-yellow.svg" alt="Patreon donate button" /></a></span>
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/JarbasAl)

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
