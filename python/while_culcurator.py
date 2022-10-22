from ast import operator
from calendar import c
from distutils.command.build_scripts import first_line_re


class Culcurator(object):
    def __init__(self, fi, op, se) -> None:
        self.first = fi
        self.op = op
        self.second = se
        self.print_result()
    
    @staticmethod
    def set_num():
        return Culcurator(int(input("첫번째 수 : ")),
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
    def main():
        ls = []
        while True:
            Culcurator.set_num()
            ls.append(Culcurator.set_num())
            self.print_result()

Culcurator.main()