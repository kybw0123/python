import googletrans

#영어로된 문서를 한글로 자동번역
translator = googletrans.Translator()

str1 = '행복하세요'
result1 = translator.translate(str1, dest='en', src='auto')
print(f'{str1} => {result1.text}')

str2 = 'I am happy'
result2 = translator.translate(str1, dest='ko', src='en')
print(f'{str2} => {result2.text}')

# 라이브러리에서 사용 가능한 언어 확인
lang = googletrans.LANGUAGES
print(lang)

# 문서를 한글로 번역하는 코드 만들기
read_file_path = r'/Users/YB/Downloads/python_git/python/40Project/영어파일.txt'
with open(read_file_path, 'r') as f:
    readLines = f.readlines()  # 라인별로 읽어 저장

# 저장한거 번역하기
for lines in readLines:
    result1 = translator.translate(lines, dest='ko')
    print(result1.text)


# 번역 내용을 새 파일로 저장하는 코드 만들기
write_file_path = r'/Users/YB/Downloads/python_git/python/40Project/한글파일.txt'

for lines in readLines:
    result1 = translator.translate(lines, dest='ko')
    with open(write_file_path, 'a', encoding='UTF8') as f:
        f.write(result1.text + '\n')
