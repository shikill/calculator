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

def square_root(a):
    if a < 0:
        raise ValueError("負の数の平方根は計算できません")
    return a ** 0.5

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("有効な数値を入力してください。")

def main():
    print("=== 簡単な計算機 ===")
    operations = {
        "1": ("足し算 (+)", add, 2),
        "2": ("引き算 (-)", subtract, 2),
        "3": ("掛け算 (*)", multiply, 2),
        "4": ("割り算 (/)", divide, 2),
        "5": ("べき乗 (**)", power, 2),
        "6": ("平方根 (√)", square_root, 1),
    }
    history = []

    while True:
        print("\n演算を選択してください:")
        for key, (name, _, __) in operations.items():
            print(f"  {key}. {name}")
        print("  7. 計算履歴を表示")
        print("  8. 終了")

        choice = input("\n選択 (1-8): ").strip()

        if choice == "8":
            print("計算機を終了します。")
            break

        if choice == "7":
            if not history:
                print("履歴はありません。")
            else:
                print("\n=== 計算履歴 ===")
                for i, entry in enumerate(history, 1):
                    print(f"  {i}. {entry}")
            continue

        if choice not in operations:
            print("無効な選択です。1〜8を入力してください。")
            continue

        name, func, arity = operations[choice]
        a = get_number("数値: " if arity == 1 else "1つ目の数値: ")

        try:
            if arity == 1:
                result = func(a)
                expr = f"√{a} = {result}"
                print(f"結果: {expr}")
            else:
                b = get_number("2つ目の数値: ")
                result = func(a, b)
                expr = f"{a} {name.split()[1]} {b} = {result}"
                print(f"結果: {expr}")
            history.append(expr)
        except ValueError as e:
            print(f"エラー: {e}")

if __name__ == "__main__":
    main()
