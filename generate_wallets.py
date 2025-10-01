#!/usr/bin/env python3
import csv
import argparse
from datetime import datetime
from eth_account import Account

# 启用（未审计）HD Wallet功能：支持 BIP39/BIP44 派生
Account.enable_unaudited_hdwallet_features()

def generate_wallet(num_words: int = 12):
    # 使用 eth-account 提供的接口直接生成助记词与账户（支持 12/24 词）
    account, mnemonic = Account.create_with_mnemonic(num_words=num_words)
    return account.address, mnemonic

def main():
    parser = argparse.ArgumentParser(description="批量生成 Web3 EVM 钱包（地址 + 助记词）并保存到 CSV。")
    parser.add_argument("--count", "-n", type=int, default=10, help="生成钱包数量（默认: 10）")
    parser.add_argument("--out", "-o", type=str, default=None, help="输出 CSV 文件路径（默认: wallets_时间戳.csv）")
    parser.add_argument("--words", type=int, choices=[12, 24], default=12, help="助记词词数（12 或 24，默认: 12）")
    args = parser.parse_args()

    count = max(1, args.count)
    out_path = args.out or f"wallets_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    rows = []
    for i in range(count):
        address, mnemonic = generate_wallet(num_words=args.words)
        rows.append({
            "index": i + 1,
            "address": address,
            "mnemonic": mnemonic
        })

    # 使用 utf-8-sig 方便在 Windows/Excel 打开
    with open(out_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["index", "address", "mnemonic"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"已生成 {count} 个钱包（{args.words} 词助记词），保存至: {out_path}")
    print("重要提示：请妥善保管 CSV 文件和助记词，任何人获得助记词都可完全控制对应资产。")

if __name__ == "__main__":
    main()
