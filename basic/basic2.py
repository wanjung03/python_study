"""
- 학번 : 202633642
- 학과 : 컴퓨터공학과
- 이름 : 김완중
"""


## if, else, elif
_uname = 'hong'
_passwd = '1234'

uname = input('# 아이디를 입력하세요: ')
passwd = input('# 비번을 입력하세요: ')
if((uname == _uname) and (passwd == _passwd)):
    print('>> 로그인 성공!!')
else :
    print('>> 아이디 혹은 비번이 틀렸습니다!!')

## for
# for 기본
for i in range(3) :
    print('Hello World!')

for i in range(0,5,1) : # 시작값, 끝값, 증가값
    print(i)

for i in [10,20,30] : # 배열값을 입력으로 사용
    print(i)

# 1~10 까지 옆으로 출력
for i in range(1,11,1) :
    print(i, end=' ')

print('\n\n')

# 구구단
for i in range(1,10) :
    print(f'2 * {i} = {2*i}')

for dan in range(2,10) :
    for i in range(1,10) :
        print(f'{dan} * {i} = {dan*i}')
    print('-----------')

## while
# 앞의 로그인 예제를 3회 실패시 종료 하도록 개선해 봄.
login = False
cnt = 0
while(login == False):
    uname = input('# 아이디를 입력하세요: ')
    passwd = input('# 비번을 입력하세요: ')
    if((uname == _uname) and (passwd == _passwd)):
        login = True
    else :
        cnt += 1
        if(cnt >=3 ):
            print('>> 3회이상 틀려서 종료합니다!!')
            exit()
        else:
            print('>> 아이디 혹은 비번이 틀렸습니다!!')
print('>> 로그인 성공!!')

# for 사용시
for cnt in range(3):
    uname = input('# 아이디를 입력하세요: ')
    passwd = input('# 비번을 입력하세요: ')
    if((uname == _uname) and (passwd == _passwd)):
        print('>> 로그인 성공!!')
        break
    else:
        print('>> 아이디 혹은 비번이 틀렸습니다!!')
else:
    print('>> 3회이상 틀려서 종료합니다!!')
    exit()