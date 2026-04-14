"""
이름 : 김완중
학번 : 202633642
학과 : 컴퓨터공학과
프로그램 명 : 지출 관리 프로그램(개인 가계부)

프로그램 설명 : 사용자가 자신의 지출을 관리할 수 있는 프로그램입니다. 

- 사용자는 지출 항목과 금액을 입력하여 지출 내역을 기록할 수 있습니다.
- 사용자는 월별 지출 총액을 확인할 수 있습니다.
- 프로그램은 간단한 텍스트 기반 인터페이스를 제공하여 사용자가 쉽게 사용할 수 있도록 설계되었습니다.
"""

# 사용자 정보 (이름: 소지금)
users = {}
# 지출 내역 (날짜, 상품명, 금액 담을 딕셔너리들이 들어갈 리스트)
history = []

#현재 로그인한 사용자를 추적할 변수(None으로 초기화 : None은 아직 로그인한 사용자가 없음을 의미)
current_user = None

# 메뉴 출력 함수
def show_menu(user, money):
    print("\n--- Minimalist SpendTrack ---")
    if user is None:
        print("1. 신규등록   2. 로그인   3. 종료")
    else:
        print(f"사용자: {user}님, 소지금: {money}원")
        print("0. 입출금 내역 입력  1. 기간별 입출금 조회  2. 입출금 내역 확인  3. 종료")

# 신규 사용자 등록 함수
def register_user():
    name = input("이름을 입력하세요: ")
    if name in users:
        print("이미 존재하는 사용자입니다.")
        return None
    else:
        users[name] = 0
        print(f"{name}님이 등록되었습니다.")
        
    money = int(input("소지금을 입력하세요: "))
    users[name] = money
    print(f"환영합니다. {name}님!")
    return name

# 기존 사용자 로그인 함수
def login_user():
    name = input("이름을 입력하세요: ")
    if name in users:
        print(f"환영합니다. {name}님!")
        return name
    else:
        print("존재하지 않는 사용자입니다.")
        return None
    
# 지출 내역 입력 함수
def manage_money():
    print("\n--- 입출금 내역 입력 ---")
    print("    1. 입금    2. 출금")

    type_choice = input("선택: ")

    date = input("날짜를 입력하세요 (예: 26.xx.xx): ")
    item = input("항목을 입력하세요: ")
    amount = int(input("금액을 입력하세요: "))

    if type_choice == '1':

        users[current_user] += amount
        record_type = "입금"
    elif type_choice == '2' and users[current_user] >= amount:

        users[current_user] -= amount
        record_type = "출금"
    else:
        print("입출금 내역을 입력할 수 없습니다.")
        return

    history.append({"날짜": date, "유형": record_type, "항목": item, "금액": amount})
    print(f"{record_type} 기록이 저장되었습니다.")

# 기간별 입출금 조회 함수
def view_history():
    search_date = input("조회할 날짜를 입력하세요 (예: 26.xx: ): ")
    print(f"\n--- {search_date}의 입출금 내역 ---")

    total_income = 0 # 입금 합계
    total_spending = 0 # 지출 합계
    found = False # 내역이 존재 여부

    for record in history:
         # 기록된 날짜가 사용자가 입력한 날짜로 시작하는지 확인
         if record["날짜"].startswith(search_date):
            print(f"[{record['날짜']}] {record['유형']}: {record['항목']} | {record['금액']}원")

            if record["유형"] == "입금":
                 total_income += record["금액"]
            else:
                total_spending += record["금액"]
            found = True

    if not found:
        print("해당 날짜에 입출금 내역이 없습니다.")
    else:
        print("-"*30)
        print(f"총 입금: {total_income}원")
        print(f"총 출금: {total_spending}원")
        print(f"이달 합계: {total_income - total_spending}원")
             
# 전체 입출금 내역 확인 함수
def view_all_history():
    print(f"\n--- {current_user}님의 전체 거래 내역 ---")

    if not history:
        print("거래 내역이 없습니다.")
        return
    
    # history 리스트를 날짜 기준으로 정렬
    sorted_history = sorted(history, key=lambda x: x["날짜"])
    for record in sorted_history:
        print(f"[{record['날짜']}] {record['유형']}: {record['항목']} | {record['금액']}원")

    print("-"*30)
    print(f"현재 총 잔액: {users[current_user]}원")
    

# import functions

# --- 메인 루프 ---
while True:
    # 1. 메뉴 출력 (함수 호출)
    current_money = users[current_user] if current_user else 0 
    show_menu(current_user, current_money)
    
    choice = input("선택: ")

    if choice == '3':
        print("프로그램을 종료합니다.")
        break

    if choice == '1':
        if current_user is None:
            current_user = register_user()
        else:
            view_history()

    elif choice == '2':
        if current_user is None:
            current_user = login_user()
        else:
            # 로그인한 사용자가 이미 존재 하는 경우, 입출금 내역을 확인하는 기능으로 이동
            view_all_history()

    # 지출 내역 입력
    elif choice == '0' and current_user is not None:
        manage_money()
