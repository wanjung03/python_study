## 가상 메모리 1KB

# MEMORY_SIZE = 1024
# virtual_memory =[""] * MEMORY_SIZE

#import os

from pathlib import Path

#1. 폴더 생성
folder_name = "user_data"
folder_path = Path(folder_name)

#  폴더가 존재하지 않으면 생성(exist_ok=True는 이미 폴더가 있더라도 에러가 발생하지 않도록 함)
folder_path.mkdir(exist_ok=True)
print(f"'{folder_name}' 폴더가 생성되었습니다.")

#2. 데이터 입력받기
user_input = input("데이터를 입력하세요: ")
file_name = input("파일 이름을 입력하세요 (예: data.txt): ")

#3. 폴더 내부에 파일 저장
# / 연산자를 통해 폴더 경로와 파일 이름을 안전하게 합칠 수 있습니다.
file_path = folder_path / file_name

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(user_input)


# IF) 파일이 이미 존재하는 경우 경고 메시지 출력 
# if (folder_path / file_name).exists():
#     print("경고! : 이미 동일한 이름의 파일이 있습니다!")

print(f"성공적으로 '{file_path}'에 저장되었습니다!")




## gemini 버전
# from pathlib import Path

# # 1. 설정 및 폴더 생성
# folder_name = "user_data" # 오타 수정
# folder_path = Path(folder_name)
# folder_path.mkdir(exist_ok=True)

# # 2. 데이터 입력받기
# user_input = input("저장할 내용을 입력하세요: ")
# file_name = input("파일 이름을 입력하세요 (예: test.txt): ").strip()

# # 파일 이름이 비어있을 경우 대비
# if not file_name:
#     file_name = "default_data.txt"

# # 3. 경로 병합 및 중복 확인
# file_path = folder_path / file_name

# # pathlib의 exists()를 활용한 중복 체크
# if file_path.exists():
#     confirm = input(f"경고: '{file_name}'이 이미 존재합니다. 덮어쓸까요? (y/n): ")
#     if confirm.lower() != 'y':
#         print("작업이 취소되었습니다.")
#         exit() # 프로그램 종료 또는 적절한 예외 처리

# # 4. 파일 저장
# try:
#     # .write_text()를 사용하면 open/with 없이도 한 줄로 텍스트 저장이 가능합니다 (짧은 텍스트용)
#     file_path.write_text(user_input, encoding='utf-8')
#     print(f"\n[성공] '{file_path}'에 데이터가 저장되었습니다!")
# except Exception as e:
#     print(f"오류가 발생했습니다: {e}")