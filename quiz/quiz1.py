"""
퀴즈-1 : 계산기 만들기-1
- 두개의 숫자와 연산자를 입력받아 계산 결과를 출력하는 프로그램
- 입력은 input() 으로 받으며, 입력된 숫자값은 int()로 변환하여 계산
- 연산자는 +, -, *, / 중 하나로 입력 받음
"""

num1 = int(input('숫자를 입력하세요 :'))
num2 = int(input('숫자를 입력하세요 :'))

cal = input('연산자를 입력하세요(+, -, *, /) : ')

if(cal == '+') :
    print(f'{num1} + {num2} = {num1 + num2}')
elif(cal == '-'): 
    print(f'{num1} - {num2} = {num1 - num2}')
elif(cal == '*'): 
    print(f'{num1} * {num2} = {num1 * num2}')
elif(cal == '/'): 
    print(f'{num1} / {num2} = {num1 / num2}')