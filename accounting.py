# 导入必要的模块
import json          # 用于JSON数据的读写
import os            # 用于检查文件是否存在
from datetime import datetime  # 用于获取当前日期时间

# 定义数据保存的文件名
DATA_FILE = "accounting_data.json"

def load_data():
    """
    从本地文件加载记账数据
    如果文件不存在则返回空列表
    """
    # 检查数据文件是否存在
    if os.path.exists(DATA_FILE):
        # 打开文件并读取内容，使用utf-8编码支持中文
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    # 文件不存在时返回空列表
    return []

def save_data(data):
    """
    将记账数据保存到本地文件
    参数data: 要保存的记录列表
    """
    # 打开文件写入数据，ensure_ascii=False保证中文正常显示
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_record(record_type):
    """
    添加一条收入或支出记录
    参数record_type: 记录类型，"收入"或"支出"
    """
    # 获取用户输入的金额
    amount = float(input("请输入金额: "))
    # 获取用户输入的备注信息
    remark = input("请输入备注: ")
    # 自动获取当前日期时间，格式化为: 年-月-日 时:分:秒
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 创建记录字典
    record = {
        "type": record_type,   # 记录类型：收入/支出
        "amount": amount,      # 金额
        "remark": remark,      # 备注
        "date": date           # 日期时间
    }
    
    # 加载现有数据
    data = load_data()
    # 将新记录添加到列表末尾
    data.append(record)
    # 保存更新后的数据
    save_data(data)
    print("记录已保存!")

def show_records():
    """
    显示所有记账记录
    """
    # 加载数据
    data = load_data()
    # 如果没有记录，提示用户
    if not data:
        print("暂无记录")
        return
    
    print("\n--- 所有记录 ---")
    # 遍历所有记录，使用enumerate从1开始编号
    for i, r in enumerate(data, 1):
        # 收入显示+号，支出显示-号
        symbol = "+" if r["type"] == "收入" else "-"
        # 格式化输出，金额保留2位小数
        print(f'{i}. {r["date"]} {r["type"]} {symbol}{r["amount"]:.2f} 备注: {r["remark"]}')

def show_summary():
    """
    显示统计信息：总收入、总支出、余额
    """
    # 加载数据
    data = load_data()
    # 计算所有收入的总和
    income = sum(r["amount"] for r in data if r["type"] == "收入")
    # 计算所有支出的总和
    expense = sum(r["amount"] for r in data if r["type"] == "支出")
    # 计算当前余额 = 总收入 - 总支出
    balance = income - expense
    
    print("\n=== 统计结果 ===")
    print(f"总收入: {income:.2f}")
    print(f"总支出: {expense:.2f}")
    print(f"当前余额: {balance:.2f}")

def main():
    """
    主函数：程序入口，显示菜单并处理用户选择
    """
    # 无限循环，直到用户选择退出
    while True:
        # 显示菜单界面
        print("\n" + "="*30)
        print("简易记账本")
        print("="*30)
        print("1. 添加收入")
        print("2. 添加支出")
        print("3. 查看所有记录")
        print("4. 查看统计")
        print("5. 退出")
        print("-"*30)
        
        # 获取用户输入的选择
        choice = input("请选择操作: ")
        
        # 根据用户选择执行相应功能
        if choice == "1":
            add_record("收入")
        elif choice == "2":
            add_record("支出")
        elif choice == "3":
            show_records()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            print("感谢使用!")
            break  # 退出循环，结束程序
        else:
            print("无效选择，请重新输入")

# 程序入口点
if __name__ == "__main__":
    main()
