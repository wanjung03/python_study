"""
퀴즈-2 : 계산기 만들기-2
- 두개의 숫자와 연산자를 입력받아 게산 결과를 리턴하는 calc 함수 정의 
- 퀴즈-1과 동일한 구현을 함수를 통해 처리.
"""


num1 = int(input('숫자를 입력하세요 :'))
num2 = int(input('숫자를 입력하세요 :'))

op = input('연산자를 입력하세요(+, -, *, /) : ')

def calc(num1, num2, op):
    if(op == '+'):
        return num1 + num2
    elif(op == '-'):
        return num1 - num2
    elif(op == '*'):
        return num1 * num2
    elif(op == '/'):
        return num1 / num2
        if num2 == 0:
            return "0으로 나누는 경우 예외"
        return num1 / num2
    else:
        return "잘못된 연산자라는 오류 메시지 "

print(calc(num1, num2, op)) 
    
