class Calculator:
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2
    def culc(self):
        op = self.op
        num1 = self.num1
        num2 = self.num2      
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2
        elif op == "%":
            result = num1 % num2
        else:
            print("잘못된 연산자")
        print(f'{num1} {op} {num2} = {result}')

if __name__=="__main__":
    num1 = int(input("첫번째 수 : "))
    op = input("+ - * / % : ")
    num2 = int(input("두번째 수 : "))   
    calculator = Calculator(num1, op, num2)
    calculator.culc()