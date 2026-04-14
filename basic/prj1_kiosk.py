# 상품 목록을 저장할 딕셔너리, 키는 상품 code
menu_items = {}

# 장바구니 목록 리스트
cart = []

# 메뉴 초기화
def init_menu():
    # 메뉴 번호를 키로, 상품명과 가격을 딕셔너리로 저장
    menu_items['1'] = {"name": "아메리카노", "price": 2000}
    menu_items['2'] = {"name": "카페라떼", "price": 2500}
    menu_items['3'] = {"name": "카페모카", "price": 3000}
    menu_items['4'] = {"name": "아이스티", "price": 1500}
    menu_items['5'] = {"name": "딸기스무디", "price": 3500}

# 메뉴 출력
def print_menu():
    print("## 메가빽 카페 메뉴 ##")
    for key, item in menu_items.items():
        print(f'{key} - {item["name"]}: {item["price"]}원')
    print(f'주문수량: {len(cart)}')
    print('-'*30)

# 장바구니에 상품 추가
def add_cart(sel):
    cart.append(menu_items[sel])


# 결제
def checkout():
    print("\n\n## 결제 정보 ##")
    for item in cart:
        print(f'{item['name']} : {item['price']}원')
    print('-'*30)
    print(f'총 금액 : {sum(item['price'] for item in cart)}원')

    pay = input ('>>>> 결제를 진행할까요?(y/n) : ')
    if(pay == 'y'):
        print('결제가 완료되었습니다. 이용해 주셔서 감사합니다.\n\n\n')
        cart.clear()

# 상품 목록 초기화
init_menu()

# 메인 루프
while True:
    print_menu()
    sel = input('메뉴를 선택하세요(메뉴선택: 번호, 결제: c, 종료: q): ')
    if sel == 'c':
        checkout()
    elif sel == 'q':
        break
    else:
        add_cart(sel)

print('프로그램을 종료 합니다!!')