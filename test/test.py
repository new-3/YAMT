import json
import requests
import re
from config import Config


def translate(source_text, target_lang, source_lang="auto"):
    if not source_text or not target_lang:
        print("Not enough arguments")
        return

    google_api = "https://translate.googleapis.com/translate_a/single?client=gtx"

    headers = {
        "referer": "https://translate.google.com/",
        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
        ),
    }
    source_text = f'"{source_text}"'
    params = {
        "dt": "t",
        "sl": source_lang,
        "tl": target_lang,
        "q": source_text,
    }

    response = requests.get(google_api, headers=headers, params=params)
    translated_text = "".join([el[0] for el in response.json()[0]]).replace('"', "")
    return translated_text


def handle_escaping_characters(data):
    """This is wrapper function of translate,
       which makes translator less likely mess with escaping characters
    """

    def wrap(text):
        pattern = r'&[0-9a-z]'
        wrapped_text = re.sub(pattern, r'"\g<0>"', text)
        return wrapped_text

    def unwrap(text):
        pattern = r'"\&[0-9a-z]"'
        unwrapped_text = re.sub(pattern, lambda x: x.group(0)[1:-1], text)
        return unwrapped_text

    data = wrap(data)
    translated = translate(data, Config.target_lang)
    return unwrap(translated)


test_string = 'This is a &a"basic" test  and &1otpimus example.'
print(handle_escaping_characters(test_string))


# origin = [
#     'Applied Energistics 2',
#     '"Applied Energistics 2"',
#     'Mekanism',
#     'Industrial Foregoing',
#     '"Industrial Foregoing"',
#     '&aABC&f'
# ]
#
# translated = []
#
# for word in origin:
#     translated.append(handle_escaping_characters(word))
#
# print(translated)


# for word in origin:
#     translated.append(translate(word, 'ko'))
#
# print(translated)
