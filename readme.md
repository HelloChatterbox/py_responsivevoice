![](pyresponsive_voice.png)

Unofficial python API for [Responsive Voice](https://responsivevoice.org)

  * [Install](#install)
  * [Example](#example)
    * [Voices](#voices)
  * [Usage](#usage)
  * [Credits](#credits)
  
# Install
```python
pip install responsivevoice
```
# Example

```python
from responsive_voice import ResponsiveVoice

engine = ResponsiveVoice()
engine.say("hello world")
engine.say("hello world",
           gender=ResponsiveVoice.MALE,
           rate=0.45)

engine = ResponsiveVoice(lang=ResponsiveVoice.PORTUGUESE_BR)
file_path = engine.get_mp3(u"olá mundo")
engine.play_mp3(file_path)
```
## Voices

You can use pre defined configurations, aka, voices

```python
from responsive_voice.voices import EnglishIndia, UKEnglishMale,\
    FallbackUKEnglishMale

india = EnglishIndia()
uk = UKEnglishMale()
uk2 = FallbackUKEnglishMale()
india.say("hello world")
uk.say("hello world")
uk2.say("hello world")

```
## Usage
```python
say(sentence, mp3_file=None, lang=None, pitch=None, rate=None, vol=None, gender=None, play_cmd="mpg123 %1", blocking=True)
```
- *sentence* : The text you want to speak.
- *mp3_file* : The name of the output file. If `None`, a temporary file will be created and the text will be played in blocking mode. Otherwise it will be played without blocking.
- *pitch* : The pitch of the speaker.
- *rate* : The rate (speed) of the speaker, value between 0 and 1.
- *vol* : The volume (loudness) of the speaker, value between 0 and 1.
- *gender* : The gender of the speaker. E.g. `ResponsiveVoice.FEMALE`
- *play_cmd* : The command used to play the file.
- *blocking* : Wether the program should wait until speaking is finished or not.

```python
play_mp3(mp3_file, play_cmd="mpg123 %1", blocking=False)
```
- *mp3_file* : The name of the mp3 file you want to play.
- *play_cmd* : The command used to play the file.
- *blocking* : Wether the program should wait until playback is finished or not.

```python
get_mp3(sentence, mp3_file=None, lang=None, pitch=None, rate=None, vol=None, gender=None)
```
- *sentence* : The text you want to speak.
- *mp3_file* : The name of the output file. If `None`, this will be generated from the text.
- *pitch* : The pitch of the speaker.
- *rate* : The rate (speed) of the speaker, value between 0 and 1.
- *vol* : The volume (loudness) of the speaker, value between 0 and 1.
- *gender* : The gender of the speaker. E.g. `ResponsiveVoice.FEMALE`


## Credits

[ResponsiveVoice](https://responsivevoice.org/)

[JarbasAI](https://jarbasal.github.io)

[![Donate with Bitcoin](https://en.cryptobadges.io/badge/micro/1QJNhKM8tVv62XSUrST2vnaMXh5ADSyYP8)](https://en.cryptobadges.io/donate/1QJNhKM8tVv62XSUrST2vnaMXh5ADSyYP8)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://paypal.me/jarbasai)
<span class="badge-patreon"><a href="https://www.patreon.com/jarbasAI" title="Donate to this project using Patreon"><img src="https://img.shields.io/badge/patreon-donate-yellow.svg" alt="Patreon donate button" /></a></span>
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/JarbasAl)

