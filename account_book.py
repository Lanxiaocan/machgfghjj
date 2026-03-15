#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
简单命令行记账小程序
功能：添加收入/支出、查看记录、统计余额
数据保存在当前目录的 accounts.json 文件中
"""

import json
import os
from datetime import datetime

DATA_FILE = "accounts.json"


def load_data():
    """从文件加载记账数据"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_data(data):
    """保存记账数据到文件"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def add_record(record_type):
    """添加一条记录（收入或支出）"""
    try:
        amount = float(input("请输入金额："))
        if amount <= 0:
            print("金额必须大于0！")
            return
    except ValueError:
        print("请输入有效的数字！")
        return

    note = input("请输入备注（可选，直接回车跳过）：").strip()
    
    record = {
        "type": record_type,
        "amount": amount,
        "note": note if note else "无",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    data = load_data()
    data.append(record)
    save_data(data)
    
    print(f"✓ 已添加一条{record_type}记录：{amount}元")


def show_all():
    """显示所有记录"""
    data = load_data()
    
    if not data:
        print("暂无记录！")
        return
    
    print("\n" + "=" * 60)
    print(f"{'序号':<6}{'类型':<8}{'金额':<12}{'日期':<20}{'备注'}")
    print("=" * 60)
    
    for i, record in enumerate(data, 1):
        type_str = "收入" if record["type"] == "收入" else "支出"
        print(f"{i:<6}{type_str:<8}{record['amount']:<12}{record['date']:<20}{record['note']}")
    
    print("=" * 60)


def show_statistics():
    """统计总收入、总支出、余额"""
    data = load_data()
    
    total_income = sum(r["amount"] for r in data if r["type"] == "收入")
    total_expense = sum(r["amount"] for r in data if r["type"] == "支出")
    balance = total_income - total_expense
    
    print("\n" + "-" * 30)
    print(f"📊 统计信息")
    print("-" * 30)
    print(f"总收入：{total_income:.2f} 元")
    print(f"总支出：{total_expense:.2f} 元")
    print(f"当前余额：{balance:.2f} 元")
    print("-" * 30)


def delete_record():
    """删除指定记录"""
    data = load_data()
    
    if not data:
        print("暂无记录可删除！")
        return
    
    show_all()
    
    try:
        index = int(input("请输入要删除的记录序号："))
        if 1 <= index <= len(data):
            deleted = data.pop(index - 1)
            save_data(data)
            print(f"✓ 已删除记录：{deleted['type']} {deleted['amount']}元")
        else:
            print("序号无效！")
    except ValueError:
        print("请输入有效的数字！")


def main():
    """主程序入口"""
    print("\n📒 欢迎使用命令行记账小程序")
    
    while True:
        print("\n" + "-" * 30)
        print("1. 添加收入")
        print("2. 添加支出")
        print("3. 查看所有记录")
        print("4. 统计信息")
        print("5. 删除记录")
        print("0. 退出程序")
        print("-" * 30)
        
        choice = input("请选择操作 (0-5)：").strip()
        
        if choice == "1":
            add_record("收入")
        elif choice == "2":
            add_record("支出")
        elif choice == "3":
            show_all()
        elif choice == "4":
            show_statistics()
        elif choice == "5":
            delete_record()
        elif choice == "0":
            print("再见！感谢使用 👋")
            break
        else:
            print("无效选择，请重新输入！")


if __name__ == "__main__":
    main()
