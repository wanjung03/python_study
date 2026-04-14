# 컴퓨터공학과 / 202633642 / 김완중


## 변수 선언과 출력
num1 = 10
num2 = 20
print(num1, num2)

# 하나의 변수에 두개의 값을 할당하면 배열이됨.
a = 100, 200
print(a)
print(a[1])

## 자료형, 연산자
# 자료형 확인
print(type(123))
print(type('hello'))
print(type(12.2))
print(type([1,2,3,4]))
print(type((1,2,3,4)))
print(type({10,20,30}))
print(type({'a':10, 'b':20, 'c':30}))

# 산술 연산
print(num1 + num2)
print(num1 * num2**2 / 100)

# 비교 연산
result = num1 == num2
print(result)

if(num1 > num2):
    print('num1이 num2보다 크다')

# 논리 연산
login = False

if(num1 > 10 and num2 != 20):
    print('num1이 10보다 크고 num2가 20이 아닌 경우 실행')
if(num1 > 10 or num2 <= 20):
    print('num1이 10보다 크거나 num2가 20보다 작은 경우 실행')
if(not login):
    print('login 변수값이 false인 경우 실행')

# 할당 연산
num1 += 10 # num1 = num1 + 10
print(num1)

# 기타 연산
print(10 in [10, 20, 30])

print(1 == 1)
print(1 is 1)

print([1] == [1])
print([1] is [1])


# ----------------------------(예제)----------------------------- #


id = input('id를 입력하세요.\n')
pw = input('pw를 입력하세요.\n')

if( id == '컴공' and pw == '김완중'):
    print('<접속 성공>')
else:
    print('<접속 실패>')
    if( id == '컴공' or pw == '김완중'):
        print('id와 pw중 하나가 일치하지 않습니다.')
    else:
        print("정보가 존재하지 않습니다.")