import json
from config import Config
from translate import translate


if __name__ == '__main__':
    with open(Config.input_path, "r", encoding='utf-8') as f:
        data = json.load(f)

    result_dict = {}

    for key, value in data.items():
        print(value)
        result1 = translate(value)
        print(key + result1)
        result_dict[key] = result1

        print(key)
        result_dict[key] = result1

    print(result_dict)

    with open(Config.output_path, 'w', encoding='utf-8') as f:
        json.dump(result_dict, f, indent=4, ensure_ascii=False)
