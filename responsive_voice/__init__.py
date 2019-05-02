import requests
import subprocess
import random
import string
import os


class ResponsiveVoice(object):
    # Genders
    FEMALE = "female"
    MALE = "male"

    # Languages
    ENGLISH_GB = "en-GB"
    ENGLISH_AU = "en-AU"
    ENGLISH_US = "en-US"
    ENGLISH_ZA = "en-ZA"
    ENGLISH_IE = "en-IE"
    HEBREW = "he-IL"
    THAI = "th-TH"
    PORTUGESE_BR = "pt-BR"
    PORTUGESE_PT = "pt-PT"
    SLOVAK = "sk-SK"
    FRENCH_CA = "fr-CA"
    ROMANIAN = "ro-RO"
    NORWEGIAN = "no-NO"
    FINNISH = "fi-FI"
    POLISH = "pl-PL"
    GERMAN = "de-DE"
    DUTCH = "nl-NL"
    INDONESIAN = "id-ID"
    TURKISH = "tr-TR"
    ITALIAN = "it-IT"
    FRENCH = "fr-FR"
    RUSSIAN = "ru-RU"
    SPANISH_MX = "es-MX"
    SPANISH_ES = "es-ES"
    CHINESE_HK = "zh-HK"
    CHINESE_TW = "zh-TW"
    CHINESE_CN = "zh-CN"
    SWEDISH = "sv-SE"
    HUNGARIAN = "hu-HU"
    DUTCH_BE = "nl-BE"
    ARABIC_SA = "ar-SA"
    KOREAN = "ko-KR"
    CZECH = "cs-CZ"
    DANISH = "da-DK"
    HINDI = "hi-IN"
    GREEK = "el-GR"
    JAPANESE = "ja-JP"

    def __init__(self, lang=ENGLISH_US, pitch=0.5, rate=0.5, vol=1, gender=FEMALE):
        self.pitch = pitch
        self.rate = rate
        self.vol = vol
        self.lang = lang
        if "f" not in gender:
            self.sv = "g1"
            self.vn = "rjs"
        else:
            self.vn = self.sv = ""

    def play_mp3(self, mp3_file, play_cmd="mpg123 -q %1", blocking=False):
        play_mp3_cmd = str(play_cmd).split(" ")
        for index, cmd in enumerate(play_mp3_cmd):
            if cmd == "%1":
                play_mp3_cmd[index] = (mp3_file)
        if blocking:
            return subprocess.call(play_mp3_cmd)
        else:
            return subprocess.Popen(play_mp3_cmd)

    def get_mp3(self, sentence, mp3_file=None, lang=None, pitch=None, rate=None, vol=None, gender=None):
        if mp3_file is None:
            mp3_file = sentence.replace(" ", "_").replace("\n", "")
            if len(mp3_file) > 20:
                mp3_file = mp3_file[: 20]

        if not mp3_file.endswith(".mp3"):
            mp3_file += ".mp3"

        params = {
            "t": sentence,
            "tl": lang or self.lang,
            "pitch": pitch or self.pitch,
            "rate": rate or self.rate,
            "vol": vol or self.vol,
            "sv": "g1" if gender is not None and "f" not in gender else "",
            "vn": "rjs" if gender is not None and "f" not in gender else ""
        }

        base_url = "https://code.responsivevoice.org/getvoice.php"
        r = requests.get(base_url, params)

        with open(mp3_file, "wb") as f:
            f.write(r.content)
        return mp3_file

    def say(self, sentence, mp3_file=None, lang=None, pitch=None, rate=None, vol=None, gender=None, play_cmd="mpg123 -q %1"):
        if mp3_file is None:
            filename = "tmp_" + ''.join(random.choice(string.ascii_letters) for _ in range(10)) + ".mp3"
            blocking = True
        else:
            filename = mp3_file
            blocking = False
        filename = self.get_mp3(sentence, filename, lang=lang, pitch=pitch, rate=rate, vol=vol, gender=gender)
        self.play_mp3(filename, play_cmd, blocking=blocking)
        if mp3_file is None:
            os.remove(filename)
