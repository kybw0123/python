import qrcode

# QR코드 데이터 생성 및 QR코드 만들기
qr_data = 'https://github.com/kybw0123'
qr_img = qrcode.make(qr_data)
save_path = 'github.png'
qr_img.save(save_path)

# 텍스트 파일에 저장된 주소를 이용해 한줄씩 읽고 qr코드로 저장
file_path = 'qrcode.txt'
with open(file_path, 'rt', encoding='UTF-8') as f :
    read_lines = f.readlines()

    for line in read_lines:
        line = line.strip()
        print(line)

        qr_data = line
        qr_img = qrcode.make(qr_data)
        save_path = qr_data + '.png'
        qr_img.save(save_path)
