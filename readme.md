# 모드팩 퀘스트 (JSON) 번역기
All the Mods 9 TTS 번역을 위한 파이썬 프로그램 by new3

## 사용방법
1. 모드팩 다운 뒤 `kubejs/assets/kubejs/lang` 폴더 안의 `en_us.json`을 복사해서 `input` 폴더 안에 붙여넣기합니다.
2. `python main.py`로 main.py를 실행합니다
3. 차분히 기다립니다 (원본 파일이 450kb -> 10분 이상 소요)
4. `output` 폴더 안의 `ko_kr.json` 파일을 모드팩 폴더의 `kubejs/assets/kubejs/lang` 폴더 안에 넣고, 언어를 한국어로 설정합니다.

## 특이사항
1. &a, &f 와 같은 color fommating code를 보존해서, 번역 이후 텍스트가 깨지는는 현상을 최소화하려고 노력했습니다.
2. 모드의 이름, 광석 이름 같은 고유명사를 사전에 작성된 용어사전을 통해 미리 변환 후 번역합니다.
 - 용어사전은 config.py 내에서 수정 가능합니다.
3. 2에 따른 부작용으로 Create 같은 단어가 '만들다'의 의미로 사용되는 경우에도 그대로 크리에이트(Create) 로 변환하는 문제가 있습니다.
4. NewestAF 님의 파이썬 스크립트를 기반으로 작성했습니다.