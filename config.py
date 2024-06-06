from os import path
import os


class Config:
    __root_dir = path.dirname(path.abspath(__file__))
    __input_folder = 'input'
    __output_folder = 'output'
    __input_file = 'en_us.json'
    __output_file = 'ko_kr.json'

    target_lang = 'ko'
    input_path = path.join(__root_dir, __input_folder, __input_file)
    output_path = path.join(__root_dir, __output_folder, __output_file)

    if not path.exists(output_path):
        os.makedirs(output_path)


class Glossary:
    glossary_dictionary = {
        "mods": {
            'Apotheosis': '어포더시스(Apotheosis)',
            'Silent Gear': '사일런트 기어(Silent Gear)',
            'Applied Energistics 2': '어플라이드 에너지스틱스 2(Applied Energistics 2)',
            'Refined Storage': '리파인드 스토리지(Refined Storage)',
            'Hostile Neural Networks': '적대적 뉴럴 네트워크(HNN)',
            'Mystical Agriculture': '미스티컬 어그리컬쳐(Mystical Agriculture)',
            'Productive Bees': '프로덕티브 비(Productive Bees)',
            'Project E': '프로젝트 E(Project E)',
            'Bigger Reactors': '더 큰 리액터(Bigger Reactors)',
            'Create': '크리에이트(Create)',
            'Industrial Foregoing': '인더스트리얼 포고잉(Industrial Foregoing)',
            'Mekanism': '메카니즘(Mekanism)',
            'Powah': '파와(Powah)',
            'Thermal Series': '써멀 시리즈(Thermal Series)',
            'Ars Nouveau': '아스 누보(Ars Nouveau)',
            'Blood Magic': '블러드 매직(Blood Magic)',
            'Botania': '보타니아(Botania)',
            'Forbidden and Arcanus': '포비든 앤 아카누스(Forbidden and Arcanus)',
            'Occultism': '오컬티즘(Occultism)',
            'AlltheModium': '올더모듐(AlltheModium)'
        },
        "ores": {
            'Allthemodium': '올더모듐(Allthemodium)',
            'Vibranium': '비브라늄(Vibranium)',
            'Unobtainium': '언옵태이늄(Unobtainium)',
        }
    }