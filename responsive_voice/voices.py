from responsive_voice import ResponsiveVoice


class UKEnglishFemale(ResponsiveVoice):
    uri = "UKEnglishFemale_ResponsiveVoice"
    name = "UK English Female"
    voiceIDs = [3, 7, 171, 278, 201, 5, 1, 257, 286, 342, 258, 287, 343, 8]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class UKEnglishMale(ResponsiveVoice):
    uri = "UKEnglishMale_ResponsiveVoice"
    name = "UK English Male"
    voiceIDs = [0, 277, 202, 75, 4, 2, 256, 285, 341, 159, 6, 7]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class USEnglishFemale(ResponsiveVoice):
    uri = "USEnglishFemale_ResponsiveVoice"
    name = "US English Female"
    voiceIDs = [39, 40, 41, 42, 383, 205, 204, 43, 173, 235, 283, 339, 408, 44]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class USEnglishMale(ResponsiveVoice):
    uri = "USEnglishMale_ResponsiveVoice"
    name = "US English Male"
    voiceIDs = [234, 282, 338, 236, 284, 340, 237, 382, 2, 4, 0, 6, 7, 75, 195,
                169]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class ArabicMale(ResponsiveVoice):
    uri = "ArabicMale_ResponsiveVoice"
    name = "Arabic Male"
    voiceIDs = [96, 95, 97, 196, 388]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ar-SA", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class ArabicFemale(ResponsiveVoice):
    uri = "ArabicFemale_ResponsiveVoice"
    name = "Arabic Female"
    voiceIDs = [98]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ar-SA", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class ArmenianMale(ResponsiveVoice):
    uri = "ArmenianMale_ResponsiveVoice"
    name = "Armenian Male"
    voiceIDs = [99]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hy-AM", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class AustralianFemale(ResponsiveVoice):
    uri = "AustralianFemale_ResponsiveVoice"
    name = "Australian Female"
    voiceIDs = [276, 201, 87, 5, 88]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-AU", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class AustralianMale(ResponsiveVoice):
    uri = "AustralianMale_ResponsiveVoice"
    name = "Australian Male"
    voiceIDs = [86, 381, 386]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-AU", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class BrazilianPortugueseFemale(ResponsiveVoice):
    uri = "BrazilianPortugueseFemale_ResponsiveVoice"
    name = "Brazilian Portuguese Female"
    voiceIDs = [245, 124, 123, 125, 186, 223, 126]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class BrazilianPortugueseMale(ResponsiveVoice):
    uri = "BrazilianPortugueseMale_ResponsiveVoice"
    name = "Brazilian Portuguese Male"
    voiceIDs = [315, 332, 371, 399]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class ChineseFemale(ResponsiveVoice):
    uri = "ChineseFemale_ResponsiveVoice"
    name = "Chinese Female"
    voiceIDs = [249, 58, 59, 380, 281, 231, 155, 60, 191, 268, 297, 353, 269,
                298, 354, 409, 61]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class ChineseMale(ResponsiveVoice):
    uri = "ChineseMale_ResponsiveVoice"
    name = "Chinese Male"
    voiceIDs = [317, 334, 373, 389]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class ChineseHongKongFemale(ResponsiveVoice):
    uri = "ChineseHongKongFemale_ResponsiveVoice"
    name = "Chinese (Hong Kong) Female"
    voiceIDs = [192, 193, 232, 250, 251, 270, 299, 355, 409, 252]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-HK", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class ChineseHongKongMale(ResponsiveVoice):
    uri = "ChineseHongKongMale_ResponsiveVoice"
    name = "Chinese (Hong Kong) Male"
    voiceIDs = [318, 335, 374, 390]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-HK", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class ChineseTaiwanFemale(ResponsiveVoice):
    uri = "ChineseTaiwanFemale_ResponsiveVoice"
    name = "Chinese Taiwan Female"
    voiceIDs = [194, 233, 253, 254, 305, 322, 361, 384, 319, 336, 375, 409,
                255]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class ChineseTaiwanMale(ResponsiveVoice):
    uri = "ChineseTaiwanMale_ResponsiveVoice"
    name = "Chinese Taiwan Male"
    voiceIDs = [320, 337, 376, 391]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class CzechFemale(ResponsiveVoice):
    uri = "CzechFemale_ResponsiveVoice"
    name = "Czech Female"
    voiceIDs = [101, 100, 102, 197, 103]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="cs-CZ", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class CzechMale(ResponsiveVoice):
    uri = "CzechMale_ResponsiveVoice"
    name = "Czech Male"
    voiceIDs = [161]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="cs-CZ", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class DanishFemale(ResponsiveVoice):
    uri = "DanishFemale_ResponsiveVoice"
    name = "Danish Female"
    voiceIDs = [105, 104, 106, 198, 107]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="da-DK", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class DanishMale(ResponsiveVoice):
    uri = "DanishMale_ResponsiveVoice"
    name = "Danish Male"
    voiceIDs = [162]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="da-DK", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class DeutschFemale(ResponsiveVoice):
    uri = "DeutschFemale_ResponsiveVoice"
    name = "Deutsch Female"
    voiceIDs = [27, 28, 29, 30, 78, 170, 275, 199, 31, 261, 290, 346, 262, 291,
                347, 32]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class DeutschMale(ResponsiveVoice):
    uri = "DeutschMale_ResponsiveVoice"
    name = "Deutsch Male"
    voiceIDs = [307, 324, 363, 377, 393]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class DutchFemale(ResponsiveVoice):
    uri = "DutchFemale_ResponsiveVoice"
    name = "Dutch Female"
    voiceIDs = [243, 219, 84, 157, 158, 184, 45]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nl-NL", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class DutchMale(ResponsiveVoice):
    uri = "DutchMale_ResponsiveVoice"
    name = "Dutch Male"
    voiceIDs = [157, 220, 407]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nl-NL", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class FinnishFemale(ResponsiveVoice):
    uri = "FinnishFemale_ResponsiveVoice"
    name = "Finnish Female"
    voiceIDs = [90, 89, 91, 209, 92]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fi-FI", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class FinnishMale(ResponsiveVoice):
    uri = "FinnishMale_ResponsiveVoice"
    name = "Finnish Male"
    voiceIDs = [160]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fi-FI", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class FrenchFemale(ResponsiveVoice):
    uri = "FrenchFemale_ResponsiveVoice"
    name = "French Female"
    voiceIDs = [240, 21, 22, 23, 77, 178, 279, 210, 266, 295, 351, 304, 321,
                360, 26]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class FrenchMale(ResponsiveVoice):
    uri = "FrenchMale_ResponsiveVoice"
    name = "French Male"
    voiceIDs = [311, 328, 367, 378, 392]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class GreekFemale(ResponsiveVoice):
    uri = "GreekFemale_ResponsiveVoice"
    name = "Greek Female"
    voiceIDs = [62, 63, 80, 200, 64]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="el-GR", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class GreekMale(ResponsiveVoice):
    uri = "GreekMale_ResponsiveVoice"
    name = "Greek Male"
    voiceIDs = [163]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="el-GR", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class HindiFemale(ResponsiveVoice):
    uri = "HindiFemale_ResponsiveVoice"
    name = "Hindi Female"
    voiceIDs = [247, 66, 154, 179, 213, 259, 288, 344, 67]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hi-IN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class HindiMale(ResponsiveVoice):
    uri = "HindiMale_ResponsiveVoice"
    name = "Hindi Male"
    voiceIDs = [394]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hi-IN", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class HungarianFemale(ResponsiveVoice):
    uri = "HungarianFemale_ResponsiveVoice"
    name = "Hungarian Female"
    voiceIDs = [9, 10, 81, 214, 11]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hu-HU", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class HungarianMale(ResponsiveVoice):
    uri = "HungarianMale_ResponsiveVoice"
    name = "Hungarian Male"
    voiceIDs = [164]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hu-HU", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class IndonesianFemale(ResponsiveVoice):
    uri = "IndonesianFemale_ResponsiveVoice"
    name = "Indonesian Female"
    voiceIDs = [241, 111, 112, 180, 215, 113]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="id-ID", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class IndonesianMale(ResponsiveVoice):
    uri = "IndonesianMale_ResponsiveVoice"
    name = "Indonesian Male"
    voiceIDs = [395]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="id-ID", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class ItalianFemale(ResponsiveVoice):
    uri = "ItalianFemale_ResponsiveVoice"
    name = "Italian Female"
    voiceIDs = [242, 33, 34, 35, 36, 37, 79, 181, 216, 271, 300, 356, 38]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it-IT", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class ItalianMale(ResponsiveVoice):
    uri = "ItalianMale_ResponsiveVoice"
    name = "Italian Male"
    voiceIDs = [312, 329, 368, 406]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it-IT", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class JapaneseFemale(ResponsiveVoice):
    uri = "JapaneseFemale_ResponsiveVoice"
    name = "Japanese Female"
    voiceIDs = [248, 50, 51, 280, 217, 52, 153, 182, 273, 302, 358, 274, 303,
                359, 53]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class JapaneseMale(ResponsiveVoice):
    uri = "JapaneseMale_ResponsiveVoice"
    name = "Japanese Male"
    voiceIDs = [313, 330, 369, 379, 396]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class KoreanFemale(ResponsiveVoice):
    uri = "KoreanFemale_ResponsiveVoice"
    name = "Korean Female"
    voiceIDs = [54, 55, 56, 156, 183, 218, 306, 323, 362, 384, 57]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ko-KR", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class KoreanMale(ResponsiveVoice):
    uri = "KoreanMale_ResponsiveVoice"
    name = "Korean Male"
    voiceIDs = [397]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ko-KR", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class LatinFemale(ResponsiveVoice):
    uri = "LatinFemale_ResponsiveVoice"
    voiceIDs = [114]
    deprecated = "0"
    name = "Latin Female"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="la", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class LatinMale(ResponsiveVoice):
    uri = "LatinMale_ResponsiveVoice"
    name = "Latin Male"
    voiceIDs = [165]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="la", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class NorwegianFemale(ResponsiveVoice):
    uri = "NorwegianFemale_ResponsiveVoice"
    name = "Norwegian Female"
    voiceIDs = [72, 73, 221, 74]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nb-NO", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class NorwegianMale(ResponsiveVoice):
    uri = "NorwegianMale_ResponsiveVoice"
    name = "Norwegian Male"
    voiceIDs = [166]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nb-NO", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class PolishFemale(ResponsiveVoice):
    uri = "PolishFemale_ResponsiveVoice"
    name = "Polish Female"
    voiceIDs = [244, 120, 119, 121, 185, 222, 267, 296, 352, 122]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl-PL", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class PolishMale(ResponsiveVoice):
    uri = "PolishMale_ResponsiveVoice"
    name = "Polish Male"
    voiceIDs = [314, 331, 370, 398]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl-PL", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class PortugueseFemale(ResponsiveVoice):
    uri = "PortugueseFemale_ResponsiveVoice"
    name = "Portuguese Female"
    voiceIDs = [128, 127, 129, 187, 224, 272, 301, 357, 130]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class PortugueseMale(ResponsiveVoice):
    uri = "PortugueseMale_ResponsiveVoice"
    name = "Portuguese Male"
    voiceIDs = [400]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class RomanianFemale(ResponsiveVoice):
    uri = "RomanianFemale_ResponsiveVoice"
    name = "Romanian Female"
    voiceIDs = [151, 150, 152, 225, 46]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ro-RO", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class RussianFemale(ResponsiveVoice):
    uri = "RussianFemale_ResponsiveVoice"
    name = "Russian Female"
    voiceIDs = [246, 47, 48, 83, 188, 226, 260, 289, 345, 49]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru-RU", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class RussianMale(ResponsiveVoice):
    uri = "RussianMale_ResponsiveVoice"
    name = "Russian Male"
    voiceIDs = [316, 333, 372, 387]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru-RU", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class SlovakFemale(ResponsiveVoice):
    uri = "SlovakFemale_ResponsiveVoice"
    name = "Slovak Female"
    voiceIDs = [133, 132, 134, 227, 135]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sk-SK", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class SlovakMale(ResponsiveVoice):
    uri = "SlovakMale_ResponsiveVoice"
    voiceIDs = [167]
    deprecated = "0"
    name = "Slovak Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sk-SK", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class SpanishFemale(ResponsiveVoice):
    uri = "SpanishFemale_ResponsiveVoice"
    name = "Spanish Female"
    voiceIDs = [19, 238, 16, 17, 18, 20, 76, 174, 207, 263, 292, 348, 264, 293,
                349, 15]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class SpanishMale(ResponsiveVoice):
    uri = "SpanishMale_ResponsiveVoice"
    name = "Spanish Male"
    voiceIDs = [309, 326, 365, 401]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class SpanishLatinAmericanFemale(ResponsiveVoice):
    uri = "SpanishLatinAmericanFemale_ResponsiveVoice"
    name = "Spanish Latin American Female"
    voiceIDs = [239, 137, 136, 138, 175, 208, 265, 294, 350, 139]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-MX", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class SpanishLatinAmericanMale(ResponsiveVoice):
    uri = "SpanishLatinAmericanMale_ResponsiveVoice"
    name = "Spanish Latin American Male"
    voiceIDs = [136, 310, 327, 366, 402]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-MX", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class SwedishFemale(ResponsiveVoice):
    uri = "SwedishFemale_ResponsiveVoice"
    name = "Swedish Female"
    voiceIDs = [85, 149, 228, 65]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="service-SE", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class SwedishMale(ResponsiveVoice):
    uri = "SwedishMale_ResponsiveVoice"
    name = "Swedish Male"
    voiceIDs = [148, 168]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="service-SE", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class TamilMale(ResponsiveVoice):
    uri = "TamilMale_ResponsiveVoice"
    name = "Tamil Male"
    voiceIDs = [141]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hi-IN", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class ThaiFemale(ResponsiveVoice):
    uri = "ThaiFemale_ResponsiveVoice"
    name = "Thai Female"
    voiceIDs = [143, 142, 144, 189, 229, 145]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="th-TH", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class ThaiMale(ResponsiveVoice):
    uri = "ThaiMale_ResponsiveVoice"
    name = "Thai Male"
    voiceIDs = [403]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="th-TH", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class TurkishFemale(ResponsiveVoice):
    uri = "TurkishFemale_ResponsiveVoice"
    name = "Turkish Female"
    voiceIDs = [69, 70, 82, 190, 230, 71]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="tr-TR", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class TurkishMale(ResponsiveVoice):
    uri = "TurkishMale_ResponsiveVoice"
    name = "Turkish Male"
    voiceIDs = [404]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="tr-TR", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class VietnameseFemale(ResponsiveVoice):
    uri = "VietnameseFemale_ResponsiveVoice"
    name = "Vietnamese Female"
    voiceIDs = [405]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="vi-VN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class VietnameseMale(ResponsiveVoice):
    uri = "VietnameseMale_ResponsiveVoice"
    name = "Vietnamese Male"
    voiceIDs = [146]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="vi-VN", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class AfrikaansMale(ResponsiveVoice):
    uri = "AfrikaansMale_ResponsiveVoice"
    name = "Afrikaans Male"
    voiceIDs = [93]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="af-ZA", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class AlbanianMale(ResponsiveVoice):
    uri = "AlbanianMale_ResponsiveVoice"
    name = "Albanian Male"
    voiceIDs = [94]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sq-AL", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class BosnianMale(ResponsiveVoice):
    uri = "BosnianMale_ResponsiveVoice"
    name = "Bosnian Male"
    voiceIDs = [14]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="bs", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class CatalanMale(ResponsiveVoice):
    uri = "CatalanMale_ResponsiveVoice"
    name = "Catalan Male"
    voiceIDs = [68]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ca-ES", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class CroatianMale(ResponsiveVoice):
    uri = "CroatianMale_ResponsiveVoice"
    name = "Croatian Male"
    voiceIDs = [13]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hr-HR", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class EsperantoMale(ResponsiveVoice):
    uri = "EsperantoMale_ResponsiveVoice"
    name = "Esperanto Male"
    voiceIDs = [108]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="eo", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class IcelandicMale(ResponsiveVoice):
    uri = "IcelandicMale_ResponsiveVoice"
    name = "Icelandic Male"
    voiceIDs = [110]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="is-IS", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class LatvianMale(ResponsiveVoice):
    uri = "LatvianMale_ResponsiveVoice"
    name = "Latvian Male"
    voiceIDs = [115]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="lv-LV", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MacedonianMale(ResponsiveVoice):
    uri = "MacedonianMale_ResponsiveVoice"
    name = "Macedonian Male"
    voiceIDs = [116]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="mk-MK", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MoldavianFemale(ResponsiveVoice):
    uri = "MoldavianFemale_ResponsiveVoice"
    name = "Moldavian Female"
    voiceIDs = [117]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="md", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MoldavianMale(ResponsiveVoice):
    uri = "MoldavianMale_ResponsiveVoice"
    voiceIDs = [117]
    deprecated = "0"
    name = "Moldavian Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="md", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MontenegrinMale(ResponsiveVoice):
    uri = "MontenegrinMale_ResponsiveVoice"
    name = "Montenegrin Male"
    voiceIDs = [118]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="me", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class SerbianMale(ResponsiveVoice):
    uri = "SerbianMale_ResponsiveVoice"
    name = "Serbian Male"
    voiceIDs = [12]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sr-RS", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class SerboCroatianMale(ResponsiveVoice):
    uri = "Serbo_CroatianMale_ResponsiveVoice"
    name = "Serbo-Croatian Male"
    voiceIDs = [131]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hr-HR", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class SwahiliMale(ResponsiveVoice):
    uri = "SwahiliMale_ResponsiveVoice"
    name = "Swahili Male"
    voiceIDs = [140]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sw-KE", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class WelshMale(ResponsiveVoice):
    uri = "WelshMale_ResponsiveVoice"
    name = "Welsh Male"
    voiceIDs = [147]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="cy", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class FallbackUKFemale(ResponsiveVoice):
    uri = "FallbackUKFemale_ResponsiveVoice"
    name = "Fallback UK Female"
    voiceIDs = [8]

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class FallbackenGBFemale(ResponsiveVoice):
    uri = "Fallbacken_GBFemale_ResponsiveVoice"
    name = "Fallback en-GB Female"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackHungarianFemale(ResponsiveVoice):
    uri = "FallbackHungarianFemale_ResponsiveVoice"
    name = "Fallback Hungarian Female"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hu", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackSerbianMale(ResponsiveVoice):
    uri = "FallbackSerbianMale_ResponsiveVoice"
    name = "Fallback Serbian Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sr", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackCroatianMale(ResponsiveVoice):
    uri = "FallbackCroatianMale_ResponsiveVoice"
    name = "Fallback Croatian Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hr", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackBosnianMale(ResponsiveVoice):
    uri = "FallbackBosnianMale_ResponsiveVoice"
    name = "Fallback Bosnian Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="bs", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackSpanishFemale(ResponsiveVoice):
    uri = "FallbackSpanishFemale_ResponsiveVoice"
    name = "Fallback Spanish Female"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackFrenchFemale(ResponsiveVoice):
    uri = "FallbackFrenchFemale_ResponsiveVoice"
    name = "Fallback French Female"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackDeutschFemale(ResponsiveVoice):
    uri = "FallbackDeutschFemale_ResponsiveVoice"
    name = "Fallback Deutsch Female"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackItalianFemale(ResponsiveVoice):
    uri = "FallbackItalianFemale_ResponsiveVoice"
    name = "Fallback Italian Female"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackUSEnglish(ResponsiveVoice):
    uri = "FallbackUSEnglish_ResponsiveVoice"
    name = "Fallback US English"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackDutchFemale(ResponsiveVoice):
    uri = "FallbackDutchFemale_ResponsiveVoice"
    name = "Fallback Dutch Female"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nl", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackRomanian(ResponsiveVoice):
    uri = "FallbackRomanian_ResponsiveVoice"
    name = "Fallback Romanian"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ro", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackRussian(ResponsiveVoice):
    uri = "FallbackRussian_ResponsiveVoice"
    name = "Fallback Russian"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackJapaneseFemale(ResponsiveVoice):
    uri = "FallbackJapaneseFemale_ResponsiveVoice"
    name = "Fallback Japanese Female"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackKoreanFemale(ResponsiveVoice):
    uri = "FallbackKoreanFemale_ResponsiveVoice"
    name = "Fallback Korean Female"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ko", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackChinese(ResponsiveVoice):
    uri = "FallbackChinese_ResponsiveVoice"
    name = "Fallback Chinese"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackGreek(ResponsiveVoice):
    uri = "FallbackGreek_ResponsiveVoice"
    name = "Fallback Greek"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="el", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g2")


class FallbackSwedish(ResponsiveVoice):
    uri = "FallbackSwedish_ResponsiveVoice"
    name = "Fallback Swedish"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="service", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g2")


class FallbackHindiFemale(ResponsiveVoice):
    uri = "FallbackHindiFemale_ResponsiveVoice"
    name = "Fallback Hindi Female"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hi", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackCatalan(ResponsiveVoice):
    uri = "FallbackCatalan_ResponsiveVoice"
    name = "Fallback Catalan"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ca", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackTurkish(ResponsiveVoice):
    uri = "FallbackTurkish_ResponsiveVoice"
    name = "Fallback Turkish"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="tr", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackNorwegian(ResponsiveVoice):
    uri = "FallbackNorwegian_ResponsiveVoice"
    name = "Fallback Norwegian"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="no", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackAustralianFemale(ResponsiveVoice):
    uri = "FallbackAustralianFemale_ResponsiveVoice"
    name = "Fallback Australian Female"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-AU", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackFinnish(ResponsiveVoice):
    uri = "FallbackFinnish_ResponsiveVoice"
    name = "Fallback Finnish"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fi", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackAfrikans(ResponsiveVoice):
    uri = "FallbackAfrikans_ResponsiveVoice"
    name = "Fallback Afrikans"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="af", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackAlbanian(ResponsiveVoice):
    uri = "FallbackAlbanian_ResponsiveVoice"
    name = "Fallback Albanian"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sq", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackArabic(ResponsiveVoice):
    uri = "FallbackArabic_ResponsiveVoice"
    name = "Fallback Arabic"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ar", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackArmenian(ResponsiveVoice):
    uri = "FallbackArmenian_ResponsiveVoice"
    name = "Fallback Armenian"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hy", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackCzech(ResponsiveVoice):
    uri = "FallbackCzech_ResponsiveVoice"
    name = "Fallback Czech"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="cs", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackDanish(ResponsiveVoice):
    uri = "FallbackDanish_ResponsiveVoice"
    name = "Fallback Danish"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="da", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackEsperanto(ResponsiveVoice):
    uri = "FallbackEsperanto_ResponsiveVoice"
    name = "Fallback Esperanto"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="eo", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackHaitianCreole(ResponsiveVoice):
    uri = "FallbackHaitianCreole_ResponsiveVoice"
    name = "Fallback Haitian Creole"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ht", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class FallbackIcelandic(ResponsiveVoice):
    uri = "FallbackIcelandic_ResponsiveVoice"
    name = "Fallback Icelandic"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="is", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackIndonesianFemale(ResponsiveVoice):
    uri = "FallbackIndonesianFemale_ResponsiveVoice"
    name = "Fallback Indonesian Female"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="id", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackLatinFemale(ResponsiveVoice):
    uri = "FallbackLatinFemale_ResponsiveVoice"
    name = "Fallback Latin Female"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="la", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g2")


class FallbackLatvianMale(ResponsiveVoice):
    uri = "FallbackLatvianMale_ResponsiveVoice"
    name = "Fallback Latvian Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="lv", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackMacedonianMale(ResponsiveVoice):
    uri = "FallbackMacedonianMale_ResponsiveVoice"
    name = "Fallback Macedonian Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="mk", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackMoldavianFemale(ResponsiveVoice):
    uri = "FallbackMoldavianFemale_ResponsiveVoice"
    name = "Fallback Moldavian Female"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="mo", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g2")


class FallbackMontenegrinMale(ResponsiveVoice):
    uri = "FallbackMontenegrinMale_ResponsiveVoice"
    name = "Fallback Montenegrin Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sr-ME", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackPolishFemale(ResponsiveVoice):
    uri = "FallbackPolishFemale_ResponsiveVoice"
    name = "Fallback Polish Female"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackBrazilianPortugueseFemale(ResponsiveVoice):
    uri = "FallbackBrazilianPortugueseFemale_ResponsiveVoice"
    name = "Fallback Brazilian Portuguese Female"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackPortuguese(ResponsiveVoice):
    uri = "FallbackPortuguese_ResponsiveVoice"
    name = "Fallback Portuguese"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-PT", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackSerboCroation(ResponsiveVoice):
    uri = "FallbackSerbo_Croation_ResponsiveVoice"
    name = "Fallback Serbo-Croation"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sh", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g2")


class FallbackSlovak(ResponsiveVoice):
    uri = "FallbackSlovak_ResponsiveVoice"
    name = "Fallback Slovak"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sk", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackSpanishLatinAmericanFemale(ResponsiveVoice):
    uri = "FallbackSpanishLatinAmericanFemale_ResponsiveVoice"
    name = "Fallback Spanish (Latin American) Female"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-419", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackSwahili(ResponsiveVoice):
    uri = "FallbackSwahili_ResponsiveVoice"
    name = "Fallback Swahili"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sw", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackTamil(ResponsiveVoice):
    uri = "FallbackTamil_ResponsiveVoice"
    name = "Fallback Tamil"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ta", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackThaiFemale(ResponsiveVoice):
    uri = "FallbackThaiFemale_ResponsiveVoice"
    name = "Fallback Thai Female"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="th", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackVietnameseMale(ResponsiveVoice):
    uri = "FallbackVietnameseMale_ResponsiveVoice"
    name = "Fallback Vietnamese Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="vi", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class FallbackWelsh(ResponsiveVoice):
    uri = "FallbackWelsh_ResponsiveVoice"
    name = "Fallback Welsh"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="cy", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackUKEnglishMale(ResponsiveVoice):
    uri = "FallbackUKEnglishMale_ResponsiveVoice"
    name = "Fallback UK English Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="rjs", service="g1")


class FinnishMale2(ResponsiveVoice):
    uri = "FinnishMale_ResponsiveVoice"
    name = "Finnish Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fi", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class CzechMale2(ResponsiveVoice):
    uri = "CzechMale_ResponsiveVoice"
    name = "Czech Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="cs", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class DanishMale2(ResponsiveVoice):
    uri = "DanishMale_ResponsiveVoice"
    name = "Danish Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="da", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class GreekMale2(ResponsiveVoice):
    uri = "GreekMale_ResponsiveVoice"
    name = "Greek Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="el", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class HungarianMale2(ResponsiveVoice):
    uri = "HungarianMale_ResponsiveVoice"
    name = "Hungarian Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hu", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class LatinMale2(ResponsiveVoice):
    uri = "LatinMale_ResponsiveVoice"
    name = "Latin Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="la", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class NorwegianMale2(ResponsiveVoice):
    uri = "NorwegianMale_ResponsiveVoice"
    name = "Norwegian Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="no", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class SlovakMale2(ResponsiveVoice):
    uri = "SlovakMale_ResponsiveVoice"
    name = "Slovak Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sk", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class SwedishMale2(ResponsiveVoice):
    uri = "SwedishMale_ResponsiveVoice"
    name = "Swedish Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="service", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class FallbackUSEnglishMale(ResponsiveVoice):
    uri = "FallbackUSEnglishMale_ResponsiveVoice"
    name = "Fallback US English Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class GermanGermany(ResponsiveVoice):
    uri = "GermanGermany_ResponsiveVoice"
    name = "German Germany"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de_DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class EnglishUnitedKingdom(ResponsiveVoice):
    uri = "EnglishUnitedKingdom_ResponsiveVoice"
    name = "English United Kingdom"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en_GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class EnglishIndia(ResponsiveVoice):
    uri = "EnglishIndia_ResponsiveVoice"
    name = "English India"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en_IN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class EnglishUnitedStates(ResponsiveVoice):
    uri = "EnglishUnitedStates_ResponsiveVoice"
    name = "English United States"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en_US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class SpanishSpain(ResponsiveVoice):
    uri = "SpanishSpain_ResponsiveVoice"
    name = "Spanish Spain"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es_ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class SpanishMexico(ResponsiveVoice):
    uri = "SpanishMexico_ResponsiveVoice"
    name = "Spanish Mexico"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es_MX", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class SpanishUnitedStates(ResponsiveVoice):
    uri = "SpanishUnitedStates_ResponsiveVoice"
    name = "Spanish United States"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es_US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class FrenchBelgium(ResponsiveVoice):
    uri = "FrenchBelgium_ResponsiveVoice"
    name = "French Belgium"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr_BE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class FrenchFrance(ResponsiveVoice):
    uri = "FrenchFrance_ResponsiveVoice"
    name = "French France"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr_FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class HindiIndia(ResponsiveVoice):
    uri = "HindiIndia_ResponsiveVoice"
    name = "Hindi India"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hi_IN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class IndonesianIndonesia(ResponsiveVoice):
    uri = "IndonesianIndonesia_ResponsiveVoice"
    name = "Indonesian Indonesia"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="in_ID", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class ItalianItaly(ResponsiveVoice):
    uri = "ItalianItaly_ResponsiveVoice"
    name = "Italian Italy"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it_IT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class JapaneseJapan(ResponsiveVoice):
    uri = "JapaneseJapan_ResponsiveVoice"
    name = "Japanese Japan"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja_JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class KoreanSouthKorea(ResponsiveVoice):
    uri = "KoreanSouthKorea_ResponsiveVoice"
    name = "Korean South Korea"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ko_KR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class DutchNetherlands(ResponsiveVoice):
    uri = "DutchNetherlands_ResponsiveVoice"
    name = "Dutch Netherlands"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nl_NL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class PolishPoland(ResponsiveVoice):
    uri = "PolishPoland_ResponsiveVoice"
    name = "Polish Poland"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl_PL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class PortugueseBrazil(ResponsiveVoice):
    uri = "PortugueseBrazil_ResponsiveVoice"
    name = "Portuguese Brazil"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt_BR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class PortuguesePortugal(ResponsiveVoice):
    uri = "PortuguesePortugal_ResponsiveVoice"
    name = "Portuguese Portugal"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt_PT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class RussianRussia(ResponsiveVoice):
    uri = "RussianRussia_ResponsiveVoice"
    name = "Russian Russia"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru_RU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class ThaiThailand(ResponsiveVoice):
    uri = "ThaiThailand_ResponsiveVoice"
    name = "Thai Thailand"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="th_TH", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class TurkishTurkey(ResponsiveVoice):
    uri = "TurkishTurkey_ResponsiveVoice"
    name = "Turkish Turkey"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="tr_TR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class ChineseChina(ResponsiveVoice):
    uri = "ChineseChina_ResponsiveVoice"
    name = "Chinese China"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh_CN_#Hans",
                         gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class ChineseHongKong(ResponsiveVoice):
    uri = "ChineseHongKong_ResponsiveVoice"
    name = "Chinese Hong Kong"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh_HK_#Hans",
                         gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class ChineseHongKong2(ResponsiveVoice):
    uri = "ChineseHongKong_ResponsiveVoice"
    name = "Chinese Hong Kong"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh_HK_#Hant",
                         gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class ChineseTaiwan(ResponsiveVoice):
    uri = "ChineseTaiwan_ResponsiveVoice"
    name = "Chinese Taiwan"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh_TW_#Hant",
                         gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Maged(ResponsiveVoice):
    uri = "Maged_ResponsiveVoice"
    name = "Maged"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ar-SA", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Zuzana(ResponsiveVoice):
    uri = "Zuzana_ResponsiveVoice"
    name = "Zuzana"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="cs-CZ", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Sara(ResponsiveVoice):
    uri = "Sara_ResponsiveVoice"
    name = "Sara"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="da-DK", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Anna(ResponsiveVoice):
    uri = "Anna_ResponsiveVoice"
    name = "Anna"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Melina(ResponsiveVoice):
    uri = "Melina_ResponsiveVoice"
    name = "Melina"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="el-GR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Karen(ResponsiveVoice):
    uri = "Karen_ResponsiveVoice"
    name = "Karen"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-AU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Daniel(ResponsiveVoice):
    uri = "Daniel_ResponsiveVoice"
    name = "Daniel"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Moira(ResponsiveVoice):
    uri = "Moira_ResponsiveVoice"
    name = "Moira"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-IE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class SamanthaEnhanced(ResponsiveVoice):
    uri = "SamanthaEnhanced_ResponsiveVoice"
    name = "Samantha (Enhanced)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Samantha(ResponsiveVoice):
    uri = "Samantha_ResponsiveVoice"
    name = "Samantha"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Tessa(ResponsiveVoice):
    uri = "Tessa_ResponsiveVoice"
    name = "Tessa"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-ZA", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Monica(ResponsiveVoice):
    uri = "Monica_ResponsiveVoice"
    name = "Monica"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Paulina(ResponsiveVoice):
    uri = "Paulina_ResponsiveVoice"
    name = "Paulina"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-MX", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Satu(ResponsiveVoice):
    uri = "Satu_ResponsiveVoice"
    name = "Satu"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fi-FI", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Amelie(ResponsiveVoice):
    uri = "Amelie_ResponsiveVoice"
    name = "Amelie"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-CA", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Thomas(ResponsiveVoice):
    uri = "Thomas_ResponsiveVoice"
    name = "Thomas"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Carmit(ResponsiveVoice):
    uri = "Carmit_ResponsiveVoice"
    name = "Carmit"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="he-IL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Lekha(ResponsiveVoice):
    uri = "Lekha_ResponsiveVoice"
    name = "Lekha"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hi-IN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Mariska(ResponsiveVoice):
    uri = "Mariska_ResponsiveVoice"
    name = "Mariska"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hu-HU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Damayanti(ResponsiveVoice):
    uri = "Damayanti_ResponsiveVoice"
    name = "Damayanti"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="id-ID", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Alice(ResponsiveVoice):
    uri = "Alice_ResponsiveVoice"
    name = "Alice"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it-IT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Kyoko(ResponsiveVoice):
    uri = "Kyoko_ResponsiveVoice"
    name = "Kyoko"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Yuna(ResponsiveVoice):
    uri = "Yuna_ResponsiveVoice"
    name = "Yuna"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ko-KR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Ellen(ResponsiveVoice):
    uri = "Ellen_ResponsiveVoice"
    name = "Ellen"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nl-BE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Xander(ResponsiveVoice):
    uri = "Xander_ResponsiveVoice"
    name = "Xander"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nl-NL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Nora(ResponsiveVoice):
    uri = "Nora_ResponsiveVoice"
    name = "Nora"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="no-NO", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Zosia(ResponsiveVoice):
    uri = "Zosia_ResponsiveVoice"
    name = "Zosia"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl-PL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Luciana(ResponsiveVoice):
    uri = "Luciana_ResponsiveVoice"
    name = "Luciana"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Joana(ResponsiveVoice):
    uri = "Joana_ResponsiveVoice"
    name = "Joana"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-PT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Ioana(ResponsiveVoice):
    uri = "Ioana_ResponsiveVoice"
    name = "Ioana"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ro-RO", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Milena(ResponsiveVoice):
    uri = "Milena_ResponsiveVoice"
    name = "Milena"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru-RU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Laura(ResponsiveVoice):
    uri = "Laura_ResponsiveVoice"
    name = "Laura"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="sk-SK", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Alva(ResponsiveVoice):
    uri = "Alva_ResponsiveVoice"
    name = "Alva"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="service-SE",
                         gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Kanya(ResponsiveVoice):
    uri = "Kanya_ResponsiveVoice"
    name = "Kanya"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="th-TH", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Yelda(ResponsiveVoice):
    uri = "Yelda_ResponsiveVoice"
    name = "Yelda"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="tr-TR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class TingTing(ResponsiveVoice):
    uri = "Ting_Ting_ResponsiveVoice"
    name = "Ting-Ting"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class SinJi(ResponsiveVoice):
    uri = "Sin_Ji_ResponsiveVoice"
    name = "Sin-Ji"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-HK", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MeiJia(ResponsiveVoice):
    uri = "Mei_Jia_ResponsiveVoice"
    name = "Mei-Jia"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftDavidMobileEnglishUnitedStates(ResponsiveVoice):
    uri = "MicrosoftDavidMobile_EnglishUnitedStates_ResponsiveVoice"
    name = "Microsoft David Mobile - English (United States)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftZiraMobileEnglishUnitedStates(ResponsiveVoice):
    uri = "MicrosoftZiraMobile_EnglishUnitedStates_ResponsiveVoice"
    name = "Microsoft Zira Mobile - English (United States)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftMarkMobileEnglishUnitedStates(ResponsiveVoice):
    uri = "MicrosoftMarkMobile_EnglishUnitedStates_ResponsiveVoice"
    name = "Microsoft Mark Mobile - English (United States)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class FallbackChineseHongKongFemale(ResponsiveVoice):
    uri = "FallbackChineseHongKongFemale_ResponsiveVoice"
    name = "Fallback Chinese (Hong Kong) Female"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-HK", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackChineseTaiwanFemale(ResponsiveVoice):
    uri = "FallbackChineseTaiwanFemale_ResponsiveVoice"
    name = "Fallback Chinese (Taiwan) Female"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class MicrosoftGeorgeMobileEnglishUnitedKingdom(ResponsiveVoice):
    uri = "MicrosoftGeorgeMobile_EnglishUnitedKingdom_ResponsiveVoice"
    name = "Microsoft George Mobile - English (United Kingdom)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftSusanMobileEnglishUnitedKingdom(ResponsiveVoice):
    uri = "MicrosoftSusanMobile_EnglishUnitedKingdom_ResponsiveVoice"
    name = "Microsoft Susan Mobile - English (United Kingdom)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHazelMobileEnglishUnitedKingdom(ResponsiveVoice):
    uri = "MicrosoftHazelMobile_EnglishUnitedKingdom_ResponsiveVoice"
    name = "Microsoft Hazel Mobile - English (United Kingdom)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHeeraMobileEnglishIndia(ResponsiveVoice):
    uri = "MicrosoftHeeraMobile_EnglishIndia_ResponsiveVoice"
    name = "Microsoft Heera Mobile - English (India)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-In", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftIrinaMobileRussianRussia(ResponsiveVoice):
    uri = "MicrosoftIrinaMobile_RussianRussia_ResponsiveVoice"
    name = "Microsoft Irina Mobile - Russian (Russia)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru-RU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHeddaMobileGermanGermany(ResponsiveVoice):
    uri = "MicrosoftHeddaMobile_GermanGermany_ResponsiveVoice"
    name = "Microsoft Hedda Mobile - German (Germany)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftKatjaMobileGermanGermany(ResponsiveVoice):
    uri = "MicrosoftKatjaMobile_GermanGermany_ResponsiveVoice"
    name = "Microsoft Katja Mobile - German (Germany)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHelenaMobileSpanishSpain(ResponsiveVoice):
    uri = "MicrosoftHelenaMobile_SpanishSpain_ResponsiveVoice"
    name = "Microsoft Helena Mobile - Spanish (Spain)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftLauraMobileSpanishSpain(ResponsiveVoice):
    uri = "MicrosoftLauraMobile_SpanishSpain_ResponsiveVoice"
    name = "Microsoft Laura Mobile - Spanish (Spain)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftSabinaMobileSpanishMexico(ResponsiveVoice):
    uri = "MicrosoftSabinaMobile_SpanishMexico_ResponsiveVoice"
    name = "Microsoft Sabina Mobile - Spanish (Mexico)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-MX", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftJulieMobileFrenchFrance(ResponsiveVoice):
    uri = "MicrosoftJulieMobile_FrenchFrance_ResponsiveVoice"
    name = "Microsoft Julie Mobile - French (France)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftPaulinaMobilePolishPoland(ResponsiveVoice):
    uri = "MicrosoftPaulinaMobile_PolishPoland_ResponsiveVoice"
    name = "Microsoft Paulina Mobile - Polish (Poland)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl-PL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHuihuiMobileChineseSimplifiedPRC(ResponsiveVoice):
    uri = "MicrosoftHuihuiMobile_ChineseSimplifiedPRC_ResponsiveVoice"
    name = "Microsoft Huihui Mobile - Chinese (Simplified, PRC)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftYaoyaoMobileChineseSimplifiedPRC(ResponsiveVoice):
    uri = "MicrosoftYaoyaoMobile_ChineseSimplifiedPRC_ResponsiveVoice"
    name = "Microsoft Yaoyao Mobile - Chinese (Simplified, PRC)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftTracyMobileChineseTraditionalHongKongSAR(ResponsiveVoice):
    uri = "MicrosoftTracyMobile_ChineseTraditionalHongKongSAR_ResponsiveVoice"
    name = "Microsoft Tracy Mobile - Chinese (Traditional, Hong Kong S.A.R.)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftElsaMobileItalianItaly(ResponsiveVoice):
    uri = "MicrosoftElsaMobile_ItalianItaly_ResponsiveVoice"
    name = "Microsoft Elsa Mobile - Italian (Italy)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it-IT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftMariaMobilePortugueseBrazil(ResponsiveVoice):
    uri = "MicrosoftMariaMobile_PortugueseBrazil_ResponsiveVoice"
    name = "Microsoft Maria Mobile - Portuguese (Brazil)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftAyumiMobileJapaneseJapan(ResponsiveVoice):
    uri = "MicrosoftAyumiMobile_JapaneseJapan_ResponsiveVoice"
    name = "Microsoft Ayumi Mobile - Japanese (Japan)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHarukaMobileJapaneseJapan(ResponsiveVoice):
    uri = "MicrosoftHarukaMobile_JapaneseJapan_ResponsiveVoice"
    name = "Microsoft Haruka Mobile - Japanese (Japan)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Helena(ResponsiveVoice):
    uri = "Helena_ResponsiveVoice"
    name = "Helena"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Catherine(ResponsiveVoice):
    uri = "Catherine_ResponsiveVoice"
    name = "Catherine"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-AU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Arthur(ResponsiveVoice):
    uri = "Arthur_ResponsiveVoice"
    name = "Arthur"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Martha(ResponsiveVoice):
    uri = "Martha_ResponsiveVoice"
    name = "Martha"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Marie(ResponsiveVoice):
    uri = "Marie_ResponsiveVoice"
    name = "Marie"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Oren(ResponsiveVoice):
    uri = "O_ren_ResponsiveVoice"
    name = "O-ren"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Yushu(ResponsiveVoice):
    uri = "Yu_shu_ResponsiveVoice"
    name = "Yu-shu"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftDavidEnglishUnitedStates(ResponsiveVoice):
    uri = "MicrosoftDavid_EnglishUnitedStates_ResponsiveVoice"
    name = "Microsoft David - English (United States)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftZiraEnglishUnitedStates(ResponsiveVoice):
    uri = "MicrosoftZira_EnglishUnitedStates_ResponsiveVoice"
    name = "Microsoft Zira - English (United States)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftMarkEnglishUnitedStates(ResponsiveVoice):
    uri = "MicrosoftMark_EnglishUnitedStates_ResponsiveVoice"
    name = "Microsoft Mark - English (United States)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftGeorgeEnglishUnitedKingdom(ResponsiveVoice):
    uri = "MicrosoftGeorge_EnglishUnitedKingdom_ResponsiveVoice"
    name = "Microsoft George - English (United Kingdom)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftSusanEnglishUnitedKingdom(ResponsiveVoice):
    uri = "MicrosoftSusan_EnglishUnitedKingdom_ResponsiveVoice"
    name = "Microsoft Susan - English (United Kingdom)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHazelEnglishUnitedKingdom(ResponsiveVoice):
    uri = "MicrosoftHazel_EnglishUnitedKingdom_ResponsiveVoice"
    name = "Microsoft Hazel - English (United Kingdom)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHeeraEnglishIndia(ResponsiveVoice):
    uri = "MicrosoftHeera_EnglishIndia_ResponsiveVoice"
    name = "Microsoft Heera - English (India)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-In", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftIrinaRussianRussia(ResponsiveVoice):
    uri = "MicrosoftIrina_RussianRussia_ResponsiveVoice"
    name = "Microsoft Irina - Russian (Russia)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru-RU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHeddaGermanGermany(ResponsiveVoice):
    uri = "MicrosoftHedda_GermanGermany_ResponsiveVoice"
    name = "Microsoft Hedda - German (Germany)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftKatjaGermanGermany(ResponsiveVoice):
    uri = "MicrosoftKatja_GermanGermany_ResponsiveVoice"
    name = "Microsoft Katja - German (Germany)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHelenaSpanishSpain(ResponsiveVoice):
    uri = "MicrosoftHelena_SpanishSpain_ResponsiveVoice"
    name = "Microsoft Helena - Spanish (Spain)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftLauraSpanishSpain(ResponsiveVoice):
    uri = "MicrosoftLaura_SpanishSpain_ResponsiveVoice"
    name = "Microsoft Laura - Spanish (Spain)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftSabinaSpanishMexico(ResponsiveVoice):
    uri = "MicrosoftSabina_SpanishMexico_ResponsiveVoice"
    name = "Microsoft Sabina - Spanish (Mexico)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-MX", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftJulieFrenchFrance(ResponsiveVoice):
    uri = "MicrosoftJulie_FrenchFrance_ResponsiveVoice"
    name = "Microsoft Julie - French (France)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftPaulinaPolishPoland(ResponsiveVoice):
    uri = "MicrosoftPaulina_PolishPoland_ResponsiveVoice"
    name = "Microsoft Paulina - Polish (Poland)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl-PL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHuihuiChineseSimplifiedPRC(ResponsiveVoice):
    uri = "MicrosoftHuihui_ChineseSimplifiedPRC_ResponsiveVoice"
    name = "Microsoft Huihui - Chinese (Simplified, PRC)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftYaoyaoChineseSimplifiedPRC(ResponsiveVoice):
    uri = "MicrosoftYaoyao_ChineseSimplifiedPRC_ResponsiveVoice"
    name = "Microsoft Yaoyao - Chinese (Simplified, PRC)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftTracyChineseTraditionalHongKongSAR(ResponsiveVoice):
    uri = "MicrosoftTracy_ChineseTraditionalHongKongSAR_ResponsiveVoice"
    name = "Microsoft Tracy - Chinese (Traditional, Hong Kong S.A.R.)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftElsaItalianItaly(ResponsiveVoice):
    uri = "MicrosoftElsa_ItalianItaly_ResponsiveVoice"
    name = "Microsoft Elsa - Italian (Italy)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it-IT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftMariaPortugueseBrazil(ResponsiveVoice):
    uri = "MicrosoftMaria_PortugueseBrazil_ResponsiveVoice"
    name = "Microsoft Maria - Portuguese (Brazil)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftAyumiJapaneseJapan(ResponsiveVoice):
    uri = "MicrosoftAyumi_JapaneseJapan_ResponsiveVoice"
    name = "Microsoft Ayumi - Japanese (Japan)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHarukaJapaneseJapan(ResponsiveVoice):
    uri = "MicrosoftHaruka_JapaneseJapan_ResponsiveVoice"
    name = "Microsoft Haruka - Japanese (Japan)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHortenseFrenchFrance(ResponsiveVoice):
    uri = "MicrosoftHortense_FrenchFrance_ResponsiveVoice"
    name = "Microsoft Hortense - French (France)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHanhanChineseTraditionalTaiwan(ResponsiveVoice):
    uri = "MicrosoftHanhan_ChineseTraditionalTaiwan_ResponsiveVoice"
    name = "Microsoft Hanhan - Chinese (Traditional, Taiwan)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHeamiKoreanKorean(ResponsiveVoice):
    uri = "MicrosoftHeami_KoreanKorean_ResponsiveVoice"
    name = "Microsoft Heami - Korean (Korean)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ko-KR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftStefanGermanGermany(ResponsiveVoice):
    uri = "MicrosoftStefan_GermanGermany_ResponsiveVoice"
    name = "Microsoft Stefan - German (Germany)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftRaviEnglishIndia(ResponsiveVoice):
    uri = "MicrosoftRavi_EnglishIndia_ResponsiveVoice"
    name = "Microsoft Ravi - English (India)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-IN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftPabloSpanishSpain(ResponsiveVoice):
    uri = "MicrosoftPablo_SpanishSpain_ResponsiveVoice"
    name = "Microsoft Pablo - Spanish (Spain)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftRaulSpanishMexico(ResponsiveVoice):
    uri = "MicrosoftRaul_SpanishMexico_ResponsiveVoice"
    name = "Microsoft Raul - Spanish (Mexico)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-MX", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftPaulFrenchFrance(ResponsiveVoice):
    uri = "MicrosoftPaul_FrenchFrance_ResponsiveVoice"
    name = "Microsoft Paul - French (France)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftCosimoItalianItaly(ResponsiveVoice):
    uri = "MicrosoftCosimo_ItalianItaly_ResponsiveVoice"
    name = "Microsoft Cosimo - Italian (Italy)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it-IT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftIchiroJapaneseJapan(ResponsiveVoice):
    uri = "MicrosoftIchiro_JapaneseJapan_ResponsiveVoice"
    name = "Microsoft Ichiro - Japanese (Japan)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftAdamPolishPoland(ResponsiveVoice):
    uri = "MicrosoftAdam_PolishPoland_ResponsiveVoice"
    name = "Microsoft Adam - Polish (Poland)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl-PL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftDanielPortugueseBrazil(ResponsiveVoice):
    uri = "MicrosoftDaniel_PortugueseBrazil_ResponsiveVoice"
    name = "Microsoft Daniel - Portuguese (Brazil)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftPavelRussianRussia(ResponsiveVoice):
    uri = "MicrosoftPavel_RussianRussia_ResponsiveVoice"
    name = "Microsoft Pavel - Russian (Russia)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru-RU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftKangkangChineseSimplifiedPRC(ResponsiveVoice):
    uri = "MicrosoftKangkang_ChineseSimplifiedPRC_ResponsiveVoice"
    name = "Microsoft Kangkang - Chinese (Simplified, PRC)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftDannyChineseTraditionalHongKongSAR(ResponsiveVoice):
    uri = "MicrosoftDanny_ChineseTraditionalHongKongSAR_ResponsiveVoice"
    name = "Microsoft Danny - Chinese (Traditional, Hong Kong S.A.R.)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-HK", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftYatingChineseTraditionalTaiwan(ResponsiveVoice):
    uri = "MicrosoftYating_ChineseTraditionalTaiwan_ResponsiveVoice"
    name = "Microsoft Yating - Chinese (Traditional, Taiwan)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftZhiweiChineseTraditionalTaiwan(ResponsiveVoice):
    uri = "MicrosoftZhiwei_ChineseTraditionalTaiwan_ResponsiveVoice"
    name = "Microsoft Zhiwei - Chinese (Traditional, Taiwan)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHortenseMobileFrenchFrance(ResponsiveVoice):
    uri = "MicrosoftHortenseMobile_FrenchFrance_ResponsiveVoice"
    name = "Microsoft Hortense Mobile - French (France)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHanhanMobileChineseTraditionalTaiwan(ResponsiveVoice):
    uri = "MicrosoftHanhanMobile_ChineseTraditionalTaiwan_ResponsiveVoice"
    name = "Microsoft Hanhan Mobile - Chinese (Traditional, Taiwan)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHeamiMobileKoreanKorean(ResponsiveVoice):
    uri = "MicrosoftHeamiMobile_KoreanKorean_ResponsiveVoice"
    name = "Microsoft Heami Mobile - Korean (Korean)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ko-KR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftStefanMobileGermanGermany(ResponsiveVoice):
    uri = "MicrosoftStefanMobile_GermanGermany_ResponsiveVoice"
    name = "Microsoft Stefan Mobile - German (Germany)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftRaviMobileEnglishIndia(ResponsiveVoice):
    uri = "MicrosoftRaviMobile_EnglishIndia_ResponsiveVoice"
    name = "Microsoft Ravi Mobile - English (India)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-IN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftPabloMobileSpanishSpain(ResponsiveVoice):
    uri = "MicrosoftPabloMobile_SpanishSpain_ResponsiveVoice"
    name = "Microsoft Pablo Mobile - Spanish (Spain)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftRaulMobileSpanishMexico(ResponsiveVoice):
    uri = "MicrosoftRaulMobile_SpanishMexico_ResponsiveVoice"
    name = "Microsoft Raul Mobile - Spanish (Mexico)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-MX", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftPaulMobileFrenchFrance(ResponsiveVoice):
    uri = "MicrosoftPaulMobile_FrenchFrance_ResponsiveVoice"
    name = "Microsoft Paul Mobile - French (France)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftCosimoMobileItalianItaly(ResponsiveVoice):
    uri = "MicrosoftCosimoMobile_ItalianItaly_ResponsiveVoice"
    name = "Microsoft Cosimo Mobile - Italian (Italy)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it-IT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftIchiroMobileJapaneseJapan(ResponsiveVoice):
    uri = "MicrosoftIchiroMobile_JapaneseJapan_ResponsiveVoice"
    name = "Microsoft Ichiro Mobile - Japanese (Japan)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftAdamMobilePolishPoland(ResponsiveVoice):
    uri = "MicrosoftAdamMobile_PolishPoland_ResponsiveVoice"
    name = "Microsoft Adam Mobile - Polish (Poland)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl-PL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftDanielMobilePortugueseBrazil(ResponsiveVoice):
    uri = "MicrosoftDanielMobile_PortugueseBrazil_ResponsiveVoice"
    name = "Microsoft Daniel Mobile - Portuguese (Brazil)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftPavelMobileRussianRussia(ResponsiveVoice):
    uri = "MicrosoftPavelMobile_RussianRussia_ResponsiveVoice"
    name = "Microsoft Pavel Mobile - Russian (Russia)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru-RU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftKangkangMobileChineseSimplifiedPRC(ResponsiveVoice):
    uri = "MicrosoftKangkangMobile_ChineseSimplifiedPRC_ResponsiveVoice"
    name = "Microsoft Kangkang Mobile - Chinese (Simplified, PRC)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftDannyMobileChineseTraditionalHongKongSAR(ResponsiveVoice):
    uri = "MicrosoftDannyMobile_ChineseTraditionalHongKongSAR_ResponsiveVoice"
    name = "Microsoft Danny Mobile - Chinese (Traditional, Hong Kong S.A.R.)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-HK", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftYatingMobileChineseTraditionalTaiwan(ResponsiveVoice):
    uri = "MicrosoftYatingMobile_ChineseTraditionalTaiwan_ResponsiveVoice"
    name = "Microsoft Yating Mobile - Chinese (Traditional, Taiwan)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftZhiweiMobileChineseTraditionalTaiwan(ResponsiveVoice):
    uri = "MicrosoftZhiweiMobile_ChineseTraditionalTaiwan_ResponsiveVoice"
    name = "Microsoft Zhiwei Mobile - Chinese (Traditional, Taiwan)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftDavidDesktopEnglishUnitedStates(ResponsiveVoice):
    uri = "MicrosoftDavidDesktop_EnglishUnitedStates_ResponsiveVoice"
    name = "Microsoft David Desktop - English (United States)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftZiraDesktopEnglishUnitedStates(ResponsiveVoice):
    uri = "MicrosoftZiraDesktop_EnglishUnitedStates_ResponsiveVoice"
    name = "Microsoft Zira Desktop - English (United States)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftMarkDesktopEnglishUnitedStates(ResponsiveVoice):
    uri = "MicrosoftMarkDesktop_EnglishUnitedStates_ResponsiveVoice"
    name = "Microsoft Mark Desktop - English (United States)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftGeorgeDesktopEnglishUnitedKingdom(ResponsiveVoice):
    uri = "MicrosoftGeorgeDesktop_EnglishUnitedKingdom_ResponsiveVoice"
    name = "Microsoft George Desktop - English (United Kingdom)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftSusanDesktopEnglishUnitedKingdom(ResponsiveVoice):
    uri = "MicrosoftSusanDesktop_EnglishUnitedKingdom_ResponsiveVoice"
    name = "Microsoft Susan Desktop - English (United Kingdom)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHazelDesktopEnglishUnitedKingdom(ResponsiveVoice):
    uri = "MicrosoftHazelDesktop_EnglishUnitedKingdom_ResponsiveVoice"
    name = "Microsoft Hazel Desktop - English (United Kingdom)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-GB", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHeeraDesktopEnglishIndia(ResponsiveVoice):
    uri = "MicrosoftHeeraDesktop_EnglishIndia_ResponsiveVoice"
    name = "Microsoft Heera Desktop - English (India)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-In", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftIrinaDesktopRussianRussia(ResponsiveVoice):
    uri = "MicrosoftIrinaDesktop_RussianRussia_ResponsiveVoice"
    name = "Microsoft Irina Desktop - Russian (Russia)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru-RU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHeddaDesktopGermanGermany(ResponsiveVoice):
    uri = "MicrosoftHeddaDesktop_GermanGermany_ResponsiveVoice"
    name = "Microsoft Hedda Desktop - German (Germany)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftKatjaDesktopGermanGermany(ResponsiveVoice):
    uri = "MicrosoftKatjaDesktop_GermanGermany_ResponsiveVoice"
    name = "Microsoft Katja Desktop - German (Germany)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHelenaDesktopSpanishSpain(ResponsiveVoice):
    uri = "MicrosoftHelenaDesktop_SpanishSpain_ResponsiveVoice"
    name = "Microsoft Helena Desktop - Spanish (Spain)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftLauraDesktopSpanishSpain(ResponsiveVoice):
    uri = "MicrosoftLauraDesktop_SpanishSpain_ResponsiveVoice"
    name = "Microsoft Laura Desktop - Spanish (Spain)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftSabinaDesktopSpanishMexico(ResponsiveVoice):
    uri = "MicrosoftSabinaDesktop_SpanishMexico_ResponsiveVoice"
    name = "Microsoft Sabina Desktop - Spanish (Mexico)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-MX", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftJulieDesktopFrenchFrance(ResponsiveVoice):
    uri = "MicrosoftJulieDesktop_FrenchFrance_ResponsiveVoice"
    name = "Microsoft Julie Desktop - French (France)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftPaulinaDesktopPolishPoland(ResponsiveVoice):
    uri = "MicrosoftPaulinaDesktop_PolishPoland_ResponsiveVoice"
    name = "Microsoft Paulina Desktop - Polish (Poland)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl-PL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHuihuiDesktopChineseSimplifiedPRC(ResponsiveVoice):
    uri = "MicrosoftHuihuiDesktop_ChineseSimplifiedPRC_ResponsiveVoice"
    name = "Microsoft Huihui Desktop - Chinese (Simplified, PRC)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftYaoyaoDesktopChineseSimplifiedPRC(ResponsiveVoice):
    uri = "MicrosoftYaoyaoDesktop_ChineseSimplifiedPRC_ResponsiveVoice"
    name = "Microsoft Yaoyao Desktop - Chinese (Simplified, PRC)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftTracyDesktopChineseTraditionalHongKongSAR(ResponsiveVoice):
    uri = "MicrosoftTracyDesktop_ChineseTraditionalHongKongSAR_ResponsiveVoice"
    name = "Microsoft Tracy Desktop - Chinese (Traditional, Hong Kong S.A.R.)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftElsaDesktopItalianItaly(ResponsiveVoice):
    uri = "MicrosoftElsaDesktop_ItalianItaly_ResponsiveVoice"
    name = "Microsoft Elsa Desktop - Italian (Italy)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it-IT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftMariaDesktopPortugueseBrazil(ResponsiveVoice):
    uri = "MicrosoftMariaDesktop_PortugueseBrazil_ResponsiveVoice"
    name = "Microsoft Maria Desktop - Portuguese (Brazil)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftAyumiDesktopJapaneseJapan(ResponsiveVoice):
    uri = "MicrosoftAyumiDesktop_JapaneseJapan_ResponsiveVoice"
    name = "Microsoft Ayumi Desktop - Japanese (Japan)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHarukaDesktopJapaneseJapan(ResponsiveVoice):
    uri = "MicrosoftHarukaDesktop_JapaneseJapan_ResponsiveVoice"
    name = "Microsoft Haruka Desktop - Japanese (Japan)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHortenseDesktopFrenchFrance(ResponsiveVoice):
    uri = "MicrosoftHortenseDesktop_FrenchFrance_ResponsiveVoice"
    name = "Microsoft Hortense Desktop - French (France)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHanhanDesktopChineseTraditionalTaiwan(ResponsiveVoice):
    uri = "MicrosoftHanhanDesktop_ChineseTraditionalTaiwan_ResponsiveVoice"
    name = "Microsoft Hanhan Desktop - Chinese (Traditional, Taiwan)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHeamiDesktopKoreanKorean(ResponsiveVoice):
    uri = "MicrosoftHeamiDesktop_KoreanKorean_ResponsiveVoice"
    name = "Microsoft Heami Desktop - Korean (Korean)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ko-KR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftStefanDesktopGermanGermany(ResponsiveVoice):
    uri = "MicrosoftStefanDesktop_GermanGermany_ResponsiveVoice"
    name = "Microsoft Stefan Desktop - German (Germany)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftRaviDesktopEnglishIndia(ResponsiveVoice):
    uri = "MicrosoftRaviDesktop_EnglishIndia_ResponsiveVoice"
    name = "Microsoft Ravi Desktop - English (India)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-IN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftPabloDesktopSpanishSpain(ResponsiveVoice):
    uri = "MicrosoftPabloDesktop_SpanishSpain_ResponsiveVoice"
    name = "Microsoft Pablo Desktop - Spanish (Spain)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-ES", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftRaulDesktopSpanishMexico(ResponsiveVoice):
    uri = "MicrosoftRaulDesktop_SpanishMexico_ResponsiveVoice"
    name = "Microsoft Raul Desktop - Spanish (Mexico)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-MX", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftPaulDesktopFrenchFrance(ResponsiveVoice):
    uri = "MicrosoftPaulDesktop_FrenchFrance_ResponsiveVoice"
    name = "Microsoft Paul Desktop - French (France)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftCosimoDesktopItalianItaly(ResponsiveVoice):
    uri = "MicrosoftCosimoDesktop_ItalianItaly_ResponsiveVoice"
    name = "Microsoft Cosimo Desktop - Italian (Italy)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it-IT", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftIchiroDesktopJapaneseJapan(ResponsiveVoice):
    uri = "MicrosoftIchiroDesktop_JapaneseJapan_ResponsiveVoice"
    name = "Microsoft Ichiro Desktop - Japanese (Japan)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftAdamDesktopPolishPoland(ResponsiveVoice):
    uri = "MicrosoftAdamDesktop_PolishPoland_ResponsiveVoice"
    name = "Microsoft Adam Desktop - Polish (Poland)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl-PL", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftDanielDesktopPortugueseBrazil(ResponsiveVoice):
    uri = "MicrosoftDanielDesktop_PortugueseBrazil_ResponsiveVoice"
    name = "Microsoft Daniel Desktop - Portuguese (Brazil)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftPavelDesktopRussianRussia(ResponsiveVoice):
    uri = "MicrosoftPavelDesktop_RussianRussia_ResponsiveVoice"
    name = "Microsoft Pavel Desktop - Russian (Russia)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru-RU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftKangkangDesktopChineseSimplifiedPRC(ResponsiveVoice):
    uri = "MicrosoftKangkangDesktop_ChineseSimplifiedPRC_ResponsiveVoice"
    name = "Microsoft Kangkang Desktop - Chinese (Simplified, PRC)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftDannyDesktopChineseTraditionalHongKongSAR(ResponsiveVoice):
    uri = "MicrosoftDannyDesktop_ChineseTraditionalHongKongSAR_ResponsiveVoice"
    name = "Microsoft Danny Desktop - Chinese (Traditional, Hong Kong S.A.R.)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-HK", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftYatingDesktopChineseTraditionalTaiwan(ResponsiveVoice):
    uri = "MicrosoftYatingDesktop_ChineseTraditionalTaiwan_ResponsiveVoice"
    name = "Microsoft Yating Desktop - Chinese (Traditional, Taiwan)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftZhiweiDesktopChineseTraditionalTaiwan(ResponsiveVoice):
    uri = "MicrosoftZhiweiDesktop_ChineseTraditionalTaiwan_ResponsiveVoice"
    name = "Microsoft Zhiwei Desktop - Chinese (Traditional, Taiwan)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Martin(ResponsiveVoice):
    uri = "Martin_ResponsiveVoice"
    name = "Martin"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de-DE", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class FrenchDaniel(ResponsiveVoice):
    uri = "Daniel_ResponsiveVoice"
    name = "Daniel"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr-FR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Hattori(ResponsiveVoice):
    uri = "Hattori_ResponsiveVoice"
    name = "Hattori"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja-JP", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class LiMu(ResponsiveVoice):
    uri = "Li_mu_ResponsiveVoice"
    name = "Li-mu"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Gordon(ResponsiveVoice):
    uri = "Gordon_ResponsiveVoice"
    name = "Gordon"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-AU", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Aaron(ResponsiveVoice):
    uri = "Aaron_ResponsiveVoice"
    name = "Aaron"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class Nicky(ResponsiveVoice):
    uri = "Nicky_ResponsiveVoice"
    name = "Nicky"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHanhanDesktopChineseTaiwan(ResponsiveVoice):
    uri = "MicrosoftHanhanDesktop_ChineseTaiwan_ResponsiveVoice"
    name = "Microsoft Hanhan Desktop - Chinese (Taiwan)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftHeamiDesktopKorean(ResponsiveVoice):
    uri = "MicrosoftHeamiDesktop_Korean_ResponsiveVoice"
    name = "Microsoft Heami Desktop - Korean"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ko-KR", gender=ResponsiveVoice.UNKNOWN_GENDER,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class FallbackAustralianMale(ResponsiveVoice):
    uri = "FallbackAustralianMale_ResponsiveVoice"
    name = "Fallback Australian Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-AU", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class FallbackRussianMale(ResponsiveVoice):
    uri = "FallbackRussianMale_ResponsiveVoice"
    name = "Fallback Russian Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ru", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class FallbackArabicMale(ResponsiveVoice):
    uri = "FallbackArabicMale_ResponsiveVoice"
    name = "Fallback Arabic Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ar", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class FallbackChinese2(ResponsiveVoice):
    uri = "FallbackChinese_ResponsiveVoice"
    name = "Fallback Chinese"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class FallbackChineseHK(ResponsiveVoice):
    uri = "FallbackChineseHK_ResponsiveVoice"
    name = "Fallback Chinese HK"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-HK", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class FallbackChineseTW(ResponsiveVoice):
    uri = "FallbackChineseTW_ResponsiveVoice"
    name = "Fallback Chinese TW"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-TW", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class FallbackFrenchMale(ResponsiveVoice):
    uri = "FallbackFrenchMale_ResponsiveVoice"
    name = "Fallback French Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="fr", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class FallbackDeutschMale(ResponsiveVoice):
    uri = "FallbackDeutschMale_ResponsiveVoice"
    name = "Fallback Deutsch Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="de", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class FallbackHindiMale(ResponsiveVoice):
    uri = "FallbackHindiMale_ResponsiveVoice"
    name = "Fallback Hindi Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="hi", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class FallbackIndonesianMale(ResponsiveVoice):
    uri = "FallbackIndonesianMale_ResponsiveVoice"
    name = "Fallback Indonesian Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="id", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class FallbackJapaneseMale(ResponsiveVoice):
    uri = "FallbackJapaneseMale_ResponsiveVoice"
    name = "Fallback Japanese Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ja", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class FallbackKoreanMale(ResponsiveVoice):
    uri = "FallbackKoreanMale_ResponsiveVoice"
    name = "Fallback Korean Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="ko", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class FallbackPolishMale(ResponsiveVoice):
    uri = "FallbackPolishMale_ResponsiveVoice"
    name = "Fallback Polish Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pl", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackBrazilianPortugueseMale(ResponsiveVoice):
    uri = "FallbackBrazilianPortugueseMale_ResponsiveVoice"
    name = "Fallback Brazilian Portuguese Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-BR", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class FallbackPortugueseMale(ResponsiveVoice):
    uri = "FallbackPortugueseMale_ResponsiveVoice"
    name = "Fallback Portuguese Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="pt-PT", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackSpanishMale(ResponsiveVoice):
    uri = "FallbackSpanishMale_ResponsiveVoice"
    name = "Fallback Spanish Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class FallbackSpanishLatinAmericanMale(ResponsiveVoice):
    uri = "FallbackSpanishLatinAmericanMale_ResponsiveVoice"
    name = "Fallback Spanish (Latin American) Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="es-419", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class FallbackThaiMale(ResponsiveVoice):
    uri = "FallbackThaiMale_ResponsiveVoice"
    name = "Fallback Thai Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="th", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class FallbackTurkishMale(ResponsiveVoice):
    uri = "FallbackTurkishMale_ResponsiveVoice"
    name = "Fallback Turkish Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="tr", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class FallbackVietnameseFemale(ResponsiveVoice):
    uri = "FallbackVietnameseFemale_ResponsiveVoice"
    name = "Fallback Vietnamese Female"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="vi", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g1")


class FallbackItalianMale(ResponsiveVoice):
    uri = "FallbackItalianMale_ResponsiveVoice"
    name = "Fallback Italian Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="it", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class FallbackDutchMale(ResponsiveVoice):
    uri = "FallbackDutchMale_ResponsiveVoice"
    name = "Fallback Dutch Male"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="nl", gender=ResponsiveVoice.MALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="g3")


class MicrosoftAnnaEnglishUnitedStates(ResponsiveVoice):
    uri = "MicrosoftAnna_EnglishUnitedStates_ResponsiveVoice"
    name = "Microsoft Anna - English (United States)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="en-US", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")


class MicrosoftLiliChineseChina(ResponsiveVoice):
    uri = "MicrosoftLili_ChineseChina_ResponsiveVoice"
    name = "Microsoft Lili - Chinese (China)"

    def __init__(self, pitch=0.5, rate=0.5, vol=1):
        super().__init__(lang="zh-CN", gender=ResponsiveVoice.FEMALE,
                         pitch=pitch, rate=rate, vol=vol,
                         voice_name="", service="")
