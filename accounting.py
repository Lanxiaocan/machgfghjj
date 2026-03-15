#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
纯命令行记账小程序
无需任何配置，直接运行即可使用
数据保存在本地文件 data.json 中
"""

import json
import os
from datetime import datetime

# 数据文件路径
DATA_FILE = "accounting_data.json"


def load_data():
    """从文件加载记账数据"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def save_data(records):
    """保存记账数据到文件"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


def add_record(record_type):
    """添加一条记录（收入或支出）"""
    print(f"\n--- 添加{record_type} ---")

    # 获取金额
    while True:
        try:
            amount = float(input("请输入金额: "))
            if amount <= 0:
                print("金额必须大于0，请重新输入")
                continue
            break
        except ValueError:
            print("请输入有效的数字")

    # 获取备注
    remark = input("请输入备注: ").strip()
    if not remark:
        remark = "无"

    # 自动获取当前日期
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 创建记录
    record = {
        "type": record_type,
        "amount": amount,
        "remark": remark,
        "date": date
    }

    # 加载现有数据并添加新记录
    records = load_data()
    records.append(record)
    save_data(records)

    print(f"✓ {record_type}记录添加成功！")


def view_records():
    """查看所有记录"""
    records = load_data()

    if not records:
        print("\n暂无记录")
        return

    print("\n" + "=" * 60)
    print("所有记账记录".center(56))
    print("=" * 60)
    print(f"{'序号':<6}{'类型':<8}{'金额':<12}{'日期':<20}{'备注'}")
    print("-" * 60)

    for i, record in enumerate(records, 1):
        type_str = record['type']
        amount_str = f"{record['amount']:.2f}"
        date_str = record['date']
        remark_str = record['remark'][:15]  # 备注最多显示15个字符

        # 收入和支出用不同颜色标识（如果终端支持）
        if type_str == "收入":
            type_display = f"[+]{type_str}"
        else:
            type_display = f"[-]{type_str}"

        print(f"{i:<6}{type_display:<8}{amount_str:<12}{date_str:<20}{remark_str}")

    print("=" * 60)
    print(f"共 {len(records)} 条记录")


def show_statistics():
    """统计收支情况"""
    records = load_data()

    if not records:
        print("\n暂无记录，无法统计")
        return

    # 计算总收入和总支出
    total_income = sum(r['amount'] for r in records if r['type'] == "收入")
    total_expense = sum(r['amount'] for r in records if r['type'] == "支出")
    balance = total_income - total_expense

    print("\n" + "=" * 40)
    print("收支统计".center(36))
    print("=" * 40)
    print(f"  总收入: +{total_income:.2f}")
    print(f"  总支出: -{total_expense:.2f}")
    print("-" * 40)

    # 根据余额显示不同颜色效果
    if balance >= 0:
        print(f"  当前余额: +{balance:.2f} ✓")
    else:
        print(f"  当前余额: {balance:.2f} ⚠")

    print("=" * 40)


def delete_record():
    """删除一条记录"""
    records = load_data()

    if not records:
        print("\n暂无记录可删除")
        return

    view_records()

    try:
        index = int(input("\n请输入要删除的记录序号: ")) - 1
        if 0 <= index < len(records):
            deleted = records.pop(index)
            save_data(records)
            print(f"✓ 已删除: {deleted['type']} {deleted['amount']:.2f} - {deleted['remark']}")
        else:
            print("× 无效的序号")
    except ValueError:
        print("× 请输入有效的数字")


def main():
    """主程序入口"""
    print("\n" + "=" * 40)
    print("欢迎使用命令行记账小程序".center(34))
    print("=" * 40)

    while True:
        # 显示菜单
        print("\n【主菜单】")
        print("1. 添加收入")
        print("2. 添加支出")
        print("3. 查看所有记录")
        print("4. 查看收支统计")
        print("5. 删除记录")
        print("0. 退出程序")

        choice = input("\n请选择操作 (0-5): ").strip()

        if choice == "1":
            add_record("收入")
        elif choice == "2":
            add_record("支出")
        elif choice == "3":
            view_records()
        elif choice == "4":
            show_statistics()
        elif choice == "5":
            delete_record()
        elif choice == "0":
            print("\n感谢使用，再见！")
            break
        else:
            print("\n无效的选择，请重新输入")


if __name__ == "__main__":
    main()
