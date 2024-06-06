import requests
import re
from config import Config
from config import Glossary


def __translate(source_text, target_lang, source_lang="auto"):
    """
    Basic translate function using google API.

    :param source_text:
    :param target_lang:
    :param source_lang:
    :return:
    """
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


def __process_glossary(data):
    """
    preprocesses data so that certain glossaries are replaced before getting into translation API
    :param data:
    :return:
    """
    glossary_dictionary = Glossary.glossary_dictionary

    for key, glossary_item in glossary_dictionary.items():
        pattern = re.compile(r'\b(' + '|'.join(re.escape(key) for key in glossary_item.keys()) + r')\b')
        data = pattern.sub(lambda x: glossary_item[x.group()], data)

    return data


def translate(data):
    """This is wrapper function of translate,
       which makes translator less likely mess with escaping characters
       escaping characters: &[0-9a-z] or \\n
    """

    def wrap(text):
        pattern = r'(&[0-9a-z])|(\\n)'
        wrapped_text = re.sub(pattern, r'"\g<0>"', text)
        return wrapped_text

    def unwrap(text):
        pattern = r'("&[0-9a-z]")|("\\n")'
        unwrapped_text = re.sub(pattern, lambda x: x.group(0)[1:-1], text)
        return unwrapped_text

    # format code들을 wrap하기
    data = wrap(data)

    # 용어 사전 전처리
    data = __process_glossary(data)

    # 번역 API로 처리
    data = __translate(data, Config.target_lang)

    # format code unwrap하기
    data = unwrap(data)

    return data
