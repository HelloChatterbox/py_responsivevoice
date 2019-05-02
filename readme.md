# Python Responsive Voice
[![Donate with Bitcoin](https://en.cryptobadges.io/badge/micro/1QJNhKM8tVv62XSUrST2vnaMXh5ADSyYP8)](https://en.cryptobadges.io/donate/1QJNhKM8tVv62XSUrST2vnaMXh5ADSyYP8)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://paypal.me/jarbasai)
<span class="badge-patreon"><a href="https://www.patreon.com/jarbasAI" title="Donate to this project using Patreon"><img src="https://img.shields.io/badge/patreon-donate-yellow.svg" alt="Patreon donate button" /></a></span>
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/JarbasAl)

Unofficial python API for [Responsive Voice](https: // responsivevoice.org)

## Install
```python
pip install responsivevoice
```
## Example

```python
from responsive_voice import ResponsiveVoice

engine = ResponsiveVoice()
engine.say("hello world")

engine = ResponsiveVoice(rate=0.4, vol=0.8)

engine.say("hello world", gender=ResponsiveVoice.MALE, lang=ResponsiveVoice.ENGLISH_US)

file_path = engine.get_mp3(u"ola mundo", lang=ResponsiveVoice.PORTUGESE_PT)

engine.play_mp3(file_path)
```
## Usage
`get_mp3(text, mp3_file=None, lang=None, pitch=None, rate=None, vol=None, gender=None)`
- *text*: The text you want to speak.
- *mp3_file*: The name of the output file. If `None`, this will be generated from the text.
- *lang*: The language of the speaker. E.g. `ResponsiveVoice.ENGLISH_US`
- *pitch*: The pitch of the speaker.
- *rate*: The rate (speed) of the speaker, value between 0 and 1.
- *vol*: The volume (loudness) of the speaker, value between 0 and 1.
- *gender*: The gender of the speaker. E.g. `ResponsiveVoice.FEMALE`




## Credits

JarbasAI
