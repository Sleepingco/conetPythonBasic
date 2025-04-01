todo_list = []

def show_menu():
    print("\n===== To-Do List 메뉴 =====")
    print("1. 할 일 추가")
    print("2. 할 일 삭제")
    print("3. 할 일 보기")
    print("4. 종료")

def add_task():
    task = input("추가할 할 일을 입력하세요: ")
    todo_list.append(task)
    print(f"'{task}' 추가됨.")

def delete_task():
    show_tasks()
    try:
        index = int(input("삭제할 번호를 입력하세요: ")) - 1
        if 0 <= index < len(todo_list):
            removed = todo_list.pop(index)
            print(f"'{removed}' 삭제됨.")
        else:
            print("잘못된 번호입니다.")
    except ValueError:
        print("숫자를 입력해주세요.")

def show_tasks():
    if not todo_list:
        print("할 일이 없습니다.")
    else:
        print("\n===== 현재 할 일 =====")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

# 메인 루프
while True:
    show_menu()
    choice = input("선택하세요 (1-4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        delete_task()
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 선택입니다. 1~4 중에서 선택하세요.")
