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
    HUNGARIAN = "hu-HU"
    SPANISH = "es-ES"
    FRENCH = "fr-FR"
    GERMAN = "de-DE"
    ITALIAN = "it-IT"
    ROMANIAN = "ro-RO"
    RUSSIAN = "ru-RU"
    JAPANESE = "ja-JP"
    KOREAN = "ko-KR"
    CHINESE = "zh-CN"
    GREEK = "el-GR"
    HINDI = "hi-IN"

    def __init__(self, lang=self.ENGLISH_US, pitch=0.5, rate=0.5, vol=1, gender=self.FEMALE):
        self.pitch = pitch
        self.rate = rate
        self.vol = vol
        self.lang = lang
        if "f" not in gender:
            self.sv = "g1"
            self.vn = "rjs"
        else:
            self.vn = self.sv = ""

    def play_mp3(self, mp3_file, play_cmd="mpg123 -q %1"):
        play_mp3_cmd = str(play_cmd).split(" ")
        for index, cmd in enumerate(play_mp3_cmd):
            if cmd == "%1":
                play_mp3_cmd[index] = (mp3_file)
        return subprocess.Popen(play_mp3_cmd)

    def get_mp3(self, sentence, mp3_file=None, lang=None, pitch=None, rate=None, vol=None, gender=None):
        if mp3_file is None:
            mp3_file = sentence.replace(" ", "_").replace("\n", "")
            if len(mp3_file) > 20:
                mp3_file = mp3_file[:20]

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
        with open(mp3_file, "w") as f:
            f.write(r.content)
        return mp3_file

    def say(self, sentence, mp3_file=None, lang=None, pitch=None, rate=None, vol=None, gender=None, play_cmd="mpg123 -q %1"):
        filename = "tmp_" + ''.join(random.choice(string.ascii_letters) for _ in range(10)) + ".mp3"
        self.get_mp3(sentence, filename, lang=lang, pitch=pitch, rate=rate, vol=vol, gender=gender)
        self.play_mp3(filename, play_cmd)
        os.remove(filename)
