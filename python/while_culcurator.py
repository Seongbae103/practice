from ast import operator
from calendar import c
from distutils.command.build_scripts import first_line_re


class Culcur(object):
    def __init__(self, fi, op, se) -> None:
        self.first = fi
        self.op = op
        self.second = se
        self.culc_num()
        
        
    @staticmethod
    def set_num():
        return Culcur(int(input("첫번째 수 : ")),
                      input("연산자 : "),
                      int(input("두번째 수 : ")))
    
    def culc_num(self):
        fi = self.first
        op = self.op
        se = self.second
        if op == "+":
            self.result = fi + se
        elif op == "-":
            self.result = fi - se
        elif op == "*":
            self.result = fi * se
        elif op == "/":
            self.result = fi / se
        elif op == "%":
            self.result = fi % se
        else:
            print("잘못된 연산자")

    
    def print_result(self):
        print(f"{self.first} {self.op} {self.second} = {self.result}")

    @staticmethod
    def print_end(ls):
        [i.print_result() for i in ls]

    @staticmethod
    def main():
        ls = []
        while True:
            Culcur.set_num()
            print("연산내용 : ")
            ls.append(Culcur.set_num())
            print("결과 : ")
            Culcur.print_end(ls)
            break
Culcur.main()