from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2 if num2 != 0 else "Error: Divide by zero"
        elif operation == "//":
            result = num1 // num2 if num2 != 0 else "Error: Divide by zero"
        else:
            result = "Invalid operation"
    except ValueError:
        result = "Error: Please enter valid numbers"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
