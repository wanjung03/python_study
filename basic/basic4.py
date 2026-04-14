"""
- 학번 : 202633642
- 학과 : 컴퓨터공학과
- 이름 : 김완중
"""


# 예제 사용 변수
num1 = 100
num2 = 200

## 표준 출력
# 단순 출력, sep, end 사용
print(num1,num2)
print(num1,num2, sep=',')
print('Hello', 'World', sep='-')
print('num1=',num1, ',', 'num2=',num2)  # 단순 문자열 연결은 좋지 않음.
print("A","B","C", sep='/')
print("A","B","C", end='\n\n')

# 문자열 포맷팅
name = '홍길동'
age = 20
print('이름: {0}, 나이: {1}'.format(name, age))
print('이름 3회 반복: {0}, 나이 2회 반복: {1}'.format(name*3, str(age)*2)) # 나이는 문자열로 변환해야 함.
print(f'이름: {name}, 나이: {age}') # f-string 포맷팅, 파이썬 3.8 이상