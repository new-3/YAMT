# written by NewestAF


import json
import requests


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


with open("en_us.json", "r", encoding='utf-8') as f:
    data = json.load(f)

result_dict = {}

for key, value in data.items():
    print(value)
    result1 = translate(value, "ko")
    print(key + result1)
    result_dict[key] = result1

print(result_dict)

with open('ko_kr.json', 'w', encoding='utf-8') as f:
    json.dump(result_dict, f, indent=4, ensure_ascii=False)
