"""
- 학번 : 202633642
- 학과 : 컴퓨터공학과
- 이름 : 김완중
"""
# 두 수를 합하여 결과를 리턴하는 변수
num1 = 1; num2 =2
def add(num1, num2):
    return num1 + num2
result = add(num1, num2)

print(result)

def login(id, passwd):
    if(id == 'dhkswnd' and passwd == '1234'):
        return True
    else:
        return False

# 로그인 성공 실패에 따른 메시지 출력
id = input('입력\n')
passwd = input('입력\n')

if(login(id, passwd)):
    print('환영합니다.')
else:
    print('아이디와 비번이 다릅니다.') 
# from basic.function import login (basic파일에 있는 function파일에 있는 login 함수만 사용하겠다)


# lambda 연산자 (람다는 변수를 함수 처럼 사용)
result = lambda num1, num2 : num1 + num2
print(result(10, 20))

data = [1, 2, 3, 4, 5]

for  i in data:
    print(i * 10)

for i in map(lambda x: x * 10, data):
    print(i)

# 다음주 조건문 반복문 퀴즈 있음 

