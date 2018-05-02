import urllib
import requests
import subprocess


class ResponsiveVoice(object):
    def __init__(self, lang="en-us", pitch=0.5, rate=0.5, vol=1, gender="female"):
        self.pitch = pitch
        self.rate = rate
        self.vol = vol
        self.lang = lang
        if "f" not in gender:
            self.sv = "g1"
            self.vn = "rjs"
        else:
            self.vn = self.sv = ""

    def play_mp3(self, mp3_file, play_cmd="mpg123 %1"):
        play_mp3_cmd = str(play_cmd).split(" ")
        for index, cmd in enumerate(play_mp3_cmd):
            if cmd == "%1":
                play_mp3_cmd[index] = (mp3_file)
        return subprocess.Popen(play_mp3_cmd)

    def get_mp3(self, sentence, mp3_file=None, lang=None, pitch=None, rate=None, vol=None, gender=None):
        mp3_file = mp3_file or sentence.replace(" ", "_")
        if ".mp3" not in mp3_file:
            mp3_file += ".mp3"
        params = urllib.urlencode({"t": sentence,
                                   "tl": lang or self.lang,
                                   "pitch": pitch or self.pitch,
                                   "rate": rate or self.rate,
                                   "vol": vol or self.vol,
                                   "sv": "g1" if gender is not None and "f" not in gender else "",
                                   "vn": "rjs" if gender is not None and "f" not in gender else ""})
        base_url = "http://responsivevoice.org/responsivevoice/getvoice.php"
        r = requests.get(base_url, params)
        with open(mp3_file, "w") as f:
            f.write(r.content)
        return mp3_file

    def say(self, sentence, mp3_file=None, lang=None, pitch=None, rate=None, vol=None, gender=None, play_cmd="mpg123 %1"):
        self.play_mp3(self.get_mp3(sentence, mp3_file, lang=lang, pitch=pitch, rate=rate, vol=vol, gender=gender), play_cmd)


