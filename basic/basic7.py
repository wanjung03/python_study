"""
- 학번 : 202633642
- 학과 : 컴퓨터공학과
- 이름 : 김완중
"""

# 딕셔너리는 맵 형태의 자료 구조로 key:value 로 구성
# 키와 밸류의 데이터 타입은 제한 없으며 유일해야 함. 중복될 경우 마지막 키 값이 유지됨.
dict1 = {2021001:'홍길동', 2021002:'김사랑', 2021003:'나대장'}
del(dict1[2021003])
print(dict1)
print(dict1.keys(), dict1.values()) # dict_keys, dict_values 가 붙음. 출력상 보이는 값으로 for 등에서 사용시 문제 없음.
print(list(dict1.keys()), list(dict1.values())) # dict_keys 붙지 않음.
print(dict1.items()) # 튜플 형태로 리턴

# key 로 전체값 출력
for key in dict1.keys():
    print(dict1[key])

# 전체 값만 출력
for value in dict1.values():
    print(value)

# 키가 있는지 확인, 주로 if와 사용
if(2021001 in dict1):
    print(True)