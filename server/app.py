#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return text

@app.route('/count/<int:num>')
def count(num):
    # Join numbers with newline characters
    return '\n'.join(str(i) for i in range(num))

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    try:
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == 'div':
            result = num1 / num2
        elif operation == '%':
            result = num1 % num2
        else:
            return 'Invalid operation'
    except ZeroDivisionError:
        return 'Error: Division by zero'

    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
