tasks = []

def show_menu():
    print("\n=== 待办事项列表管理器 ===")
    print("1. 添加任务")
    print("2. 查看所有任务")
    print("3. 标记任务为已完成")
    print("4. 删除任务")
    print("5. 退出程序")
    print("=========================")

def add_task():
    description = input("请输入任务描述: ")
    task = {"description": description, "completed": False}
    tasks.append(task)
    print("任务已添加!")

def view_tasks():
    if not tasks:
        print("当前没有任务。")
        return
    print("\n--- 任务列表 ---")
    for index, task in enumerate(tasks, 1):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{index}. {status} {task['description']}")

def mark_completed():
    if not tasks:
        print("当前没有任务。")
        return
    view_tasks()
    try:
        task_num = int(input("请输入要标记为完成的任务编号: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print("任务已标记为完成!")
        else:
            print("无效的任务编号。")
    except ValueError:
        print("请输入有效的数字。")

def delete_task():
    if not tasks:
        print("当前没有任务。")
        return
    view_tasks()
    try:
        task_num = int(input("请输入要删除的任务编号: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            print(f"已删除任务: {deleted_task['description']}")
        else:
            print("无效的任务编号。")
    except ValueError:
        print("请输入有效的数字。")

def main():
    while True:
        show_menu()
        choice = input("请选择操作 (1-5): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("感谢使用待办事项列表管理器!")
            break
        else:
            print("无效的选择，请输入1-5之间的数字。")

if __name__ == "__main__":
    main()
