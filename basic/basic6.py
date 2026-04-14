"""
- 학번 : 202633642
- 학과 : 컴퓨터공학과
- 이름 : 김완중
"""

## 리스트
# 리스트 선언 형태
list1 = [10, 20, 30, 40] # 직접 값을 넣어서 초기화
list2 = [i for i in range(1,10)] # 범위에 해당하는 값으로 초기화
list3 = [0 for i in range(10)] # 특정 값으로 초기화
# list3 = [0] * 10 # 특정 값으로 초기화
print(sum(list1))

# 리스트 값 조작
list1.append(50) # 마지막에 값 추가
list1[0] = 100 # 특정 위치 값 변경
list1[1:2] = [200,300] # 특정 범위 값 변경, 범위는 ~n-1 까지 인데 데이터가 더 많은 경우 추가로 삽입되는 개념, 범위가 크면 해당 위치 데이터는 삭제
list2.insert(1,2) # 1번째 인덱스 위치에 2를 삽입
del(list2[3]) # 특정 위치 값 삭제, 위치를 지정하지 않으면 전체 데이터 삭제됨
list3.remove(0) # 특정 값 삭제, 같은 값이 있을 경우 맨 먼저 나오는 값만 삭제됨

# 리스트 값 출력
print('# 리스트 값 출력')
print('list1 -> ', list1)
print('list2 -> ', list2)
print('list3 -> ', list3)
print('list1[2:5] -> ', list1[2:5]) # n-1 까지, 앞 뒤 한쪽 생략 가능
print('list1[:3] -> ', list1[:3])

# print(for i in data) # -> ERROR
print('# 람다 사용 출력')
list(map(lambda x: print(x*10, end=' '), list1)) # map 함수를 이용하여 출력
print('\n\n')

# 리스트 결합
print('# 리스트 결합 출력')
print('list1 + list2 -> ', list1 + list2) # 두개의 리스트가 연결됨
print('list1 * 3 -> ', list1 * 3) # 횟수만큼 반복

# for 문과 함께 사용시 유용한 방법들
print('# for 고급 출력')
for i, n in enumerate(list1): # 리스트로 부터 인덱스와 값을 분리해서 인자로 처리
    print(i, n)

for l1, l2 in zip(list1, list2): # 두개의 리스트로 부터 입력을 받아 처리, 짧은쪽에 맞춰짐.
    print(l1,l2)

# 기타
print('# 기타 출력')
print(len(list1))
print(list1.pop()) # 맨 마지막 값을 리턴하고 삭제
print(list1) # pop으로 50이 삭제된것 확인

print(list3.count(0)) # 특정 값이 몇개 있는지 카운트

list1.sort() # 정렬, 오름차순, 리스트 구조 변경됨.
print('list1.sort() ->', list1)

list1.sort(reverse=True) # 내림차순
print('list1.sort(reverse=True) ->', list1)

list1.reverse() # 배치 역순으로
print('list1.reverse() -> ', list1)

list4 = list1.copy() # 값을 복사한 새로운 리스트 객체
# list4 = list1 # list1을 가리키는 변수로 list1과 동일 객체
list4.append(500)
print(list1)
print(list4)
