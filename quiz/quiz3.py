"""
quiz3-3
이름을 입력받아 해당 사용자를 반환하는 함수를 작성하시오.
"""

user1 = "홍길동, 20251120, 010-1234-1234"
user2 = "김사랑, 20262021, 010-2222-3333"

my_name = input('이름을 입력하세요 : ')

def find_user(name):
    u1 = user1.split(',')
    u2 = user2.split(',')

    if u1[0] == my_name:
        return f'이름:{u1[0]}\n학번:{u1[1]}\n전화번호:{u1[2]}'
    elif u2[0] == my_name:
        return f'이름:{u2[0]}\n학번:{u2[1]}\n전화번호:{u2[2]}'
    else:
        return '사용자가 존재하지 않습니다.'
    
print(find_user(my_name))