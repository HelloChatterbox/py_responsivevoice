import requests
import subprocess


class ResponsiveVoice(object):
    # Api
    API_URL = "http://responsivevoice.org/responsivevoice/getvoice.php"

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

    def __init__(self, lang=None, pitch=0.5, rate=0.5, vol=1, gender=None):
        self.pitch = pitch
        self.rate = rate
        self.vol = vol
        self.lang = lang or ResponsiveVoice.ENGLISH_US
        self.gender = gender or ResponsiveVoice.FEMALE

    @property
    def sv(self):
        if self.gender == self.MALE:
            return "g1"
        return ""

    @property
    def vn(self):
        if self.gender == self.MALE:
            return "rjs"
        return ""

    @staticmethod
    def play_mp3(mp3_file, play_cmd="mpg123 %1"):
        play_mp3_cmd = str(play_cmd).split(" ")
        for index, cmd in enumerate(play_mp3_cmd):
            if cmd == "%1":
                play_mp3_cmd[index] = mp3_file
        return subprocess.Popen(play_mp3_cmd)

    def get_mp3(self, sentence, mp3_file=None, lang=None, pitch=None,
                rate=None, vol=None, gender=None):
        mp3_file = mp3_file or "/tmp/" + str(hash(sentence))
        if not mp3_file.endswith(".mp3"):
            mp3_file += ".mp3"

        if gender:
            sv = "g1" if "f" not in gender else "",
            vn = "rjs" if "f" not in gender else ""
        else:
            sv = self.sv
            vn = self.vn

        params = {
            "t": sentence,
            "tl": lang or self.lang,
            "pitch": pitch or self.pitch,
            "rate": rate or self.rate,
            "vol": vol or self.vol,
            "sv": sv,
            "vn": vn
        }

        r = requests.get(self.API_URL, params)
        with open(mp3_file, "wb") as f:
            f.write(r.content)
        return mp3_file

    def say(self, sentence, mp3_file=None, lang=None, pitch=None, rate=None,
            vol=None, gender=None, play_cmd="mpg123 %1"):
        filename = self.get_mp3(sentence, mp3_file, lang=lang, pitch=pitch,
                                rate=rate, vol=vol, gender=gender)
        self.play_mp3(filename, play_cmd)
