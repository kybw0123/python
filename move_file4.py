import os
import shutil

# 메인 경로
#main_path = os.getcwd() + '/'
#print(main_path)
#print(folder_path)

# file_list = os.listdir(main_path) # 파일 리스트 불러오기
# file_name =[]
# file_extension = [] #비어있는 리스트 변수 생성

# 파일 리스트에서 파일명과 확장자명 분리
class move_file:
    main_path = None
    file_list = []
    file_name = []
    file_extension = []  # 비어있는 리스트 변수 생성

    def __init__(self):
        self.main_path = os.getcwd() + '/'
        #print('경로')
        #print(self.main_path)
        self.file_list = os.listdir(self.main_path)
        #print('파일리스트')
        #print(self.file_list)
        for i in range(len(self.file_list)):
            split_file_name, split_file_extension = os.path.splitext(self.file_list[i])    #파일명과 확장자 분리
            self.file_extension.append(split_file_extension[1:])     # 비어있는 변수에 확장자 저장하기




    def foldercreate(self):
        for i in range(len(self.file_list)):
            # 생성된 폴더 확인하고 없으면 폴더 생성
            # 확장자가 없으면 폴더로 구분
            if self.file_extension[i] == "":
                print("폴더라서 넘어감")

            # py 파일은 제외 시키기
            elif self.file_extension[i] == 'py':
                print('파이썬 폴더는 안만들꺼')

            # 이미 생성된 폴더는 제외 시키기
            elif os.path.exists(self.file_extension[i]) == True :
                    print(self.file_extension[i]+' 폴더 있음')

            # 폴더가 없을때 폴더 생성 시키기
            else:
                #print("폴더 없음")
                os.mkdir(self.file_extension[i])
                print(self.file_extension[i]+'폴더 생성')

    # 파일 이동
    def movefile(self):
        # for문으로 반복시켜서 파일 이동 시키기
        print('----------------------')
        for i in range(len(self.file_list)):
            folder_path = self.main_path + self.file_extension[i]    # 이동할 폴더 경로 저장하기
            #print(folder_path)
            # 폴더는 제외시키기
            if self.file_extension[i] == "":
                print("폴더라 못옮김")

            #파이썬 파일 제외시키기
            elif self.file_extension[i] =="py":
                print("파이썬 파일이다 옮기면 안된다.")

            # 파일을 확장자에 맞춰서 올기기
            else:
                shutil.move(self.file_list[i],folder_path)
                print(self.file_list[i],"파일을",self.file_extension[i],'폴더로 이동하였습니다.')


#move = move_file()
#move.foldercreate()
#move.movefile()
# move.main_path = os.getcwd() + '/'
# move.file_list = os.listdir(move.main_path)
# move.foldercreate(move.file_list)
# move.movefile(move.file_list,move.file_extension)