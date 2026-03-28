def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("0で割ることはできません")
    return a / b

def power(a, b):
    return a ** b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("有効な数値を入力してください。")

def main():
    print("=== 簡単な計算機 ===")
    operations = {
        "1": ("足し算 (+)", add),
        "2": ("引き算 (-)", subtract),
        "3": ("掛け算 (*)", multiply),
        "4": ("割り算 (/)", divide),
        "5": ("べき乗 (**)", power),
    }

    while True:
        print("\n演算を選択してください:")
        for key, (name, _) in operations.items():
            print(f"  {key}. {name}")
        print("  6. 終了")

        choice = input("\n選択 (1-6): ").strip()

        if choice == "6":
            print("計算機を終了します。")
            break

        if choice not in operations:
            print("無効な選択です。1〜6を入力してください。")
            continue

        name, func = operations[choice]
        a = get_number("1つ目の数値: ")
        b = get_number("2つ目の数値: ")

        try:
            result = func(a, b)
            print(f"結果: {a} {name.split()[1]} {b} = {result}")
        except ValueError as e:
            print(f"エラー: {e}")

if __name__ == "__main__":
    main()
