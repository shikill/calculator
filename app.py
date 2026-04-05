import math
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def calculate(operation, a, b=None):
    if operation == "add":
        return a + b, f"{a} + {b}"
    elif operation == "subtract":
        return a - b, f"{a} - {b}"
    elif operation == "multiply":
        return a * b, f"{a} × {b}"
    elif operation == "divide":
        if b == 0:
            raise ValueError("0で割ることはできません")
        return a / b, f"{a} ÷ {b}"
    elif operation == "power":
        return a ** b, f"{a} ^ {b}"
    elif operation == "sqrt":
        if a < 0:
            raise ValueError("負の数の平方根は計算できません")
        return math.sqrt(a), f"√{a}"
    else:
        raise ValueError("不明な演算です")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calc():
    data = request.get_json()
    operation = data.get("operation")

    try:
        a = float(data.get("a", 0))
        b = float(data.get("b", 0)) if operation != "sqrt" else None

        result, expr = calculate(operation, a, b)

        display_result = int(result) if result == int(result) else result
        entry = f"{expr} = {display_result}"

        return jsonify({"result": display_result, "expr": entry})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception:
        return jsonify({"error": "計算エラーが発生しました"}), 400


if __name__ == "__main__":
    app.run(debug=True)
