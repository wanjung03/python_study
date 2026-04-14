# 데이터를 저장할 빈 딕셔너리 생성
student_data = {}

print("--- 학생 성적 등록을 시작합니다 (종료하려면 이름에 '종료' 입력) ---")

while True:
    name = input("\n학생 이름을 입력하세요: ")
    if name == "종료": break
    
    # 해당 학생의 과목과 점수를 담을 딕셔너리
    subjects = {}
    while True:
        sub_name = input(f"[{name}]의 과목명을 입력하세요 (완료 시 'n' 입력): ")
        if sub_name.lower() == 'n': break
        score = int(input(f"{sub_name} 점수를 입력하세요: "))
        subjects[sub_name] = score
    
    # 전체 데이터에 저장
    student_data[name] = subjects

print("\n" + "="*40)
print("성적 조회를 시작합니다.")
print("="*40)

while True:
    search_name = input("\n조회할 이름을 입력하세요 (종료: q): ")
    if search_name.lower() == 'q': break
    
    if search_name in student_data:
        scores = student_data[search_name]
        
        print(f"\n성적표: {search_name}")
        print("=" * 35)
        print("\t".join(scores.keys()))
        print("-" * 35)
        print("\t".join(map(str, scores.values())))
        print("=" * 35)
        
        total = sum(scores.values())
        avg = total / len(scores) if scores else 0
        print(f"총점: {total}, 평균: {avg:.2f}")
    else:
        print("등록되지 않은 학생입니다.")