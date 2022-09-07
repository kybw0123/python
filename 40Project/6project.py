# 압축파일 암호푸는 프로그램

import itertools
import zipfile

def un_zip(passwd_string, min_len, max_len, zFile):
    for len in range(min_len, max_len):
        to_attempt = itertools.product(passwd_string, repeat=len)
        for attemp in to_attempt:
            passwd = ''.join(attemp)
            print(passwd)
            try:
                zFile.extractall(pwd=passwd.encode())
                print(f"비밀번호는 {passwd} 입니다.")
                return 1
            except:
                pass


#입력할 비밀번호
passwd_string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(),./<>-_=+\|'

#비밀번호를 찾을 압축파일
zFile = zipfile.ZipFile(r'/Users/YB/Downloads/python_git/python/40Project/SCA플레이버휠+한글.png.zip')

#최소 글자, 최대 글자
min_len = 1
max_len = 5

unzip_result = un_zip(passwd_string, min_len, max_len, zFile)

if unzip_result ==1:
    print('암호찾기에 성공하였습니다.')
else:
    print('암호찾기에 실패하였습니다.')

