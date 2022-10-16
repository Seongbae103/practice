class Culcurator:
    def solution(self, a, b, c):
        title = "###Culcurator###"
        if b == "+":
            answer = a + c
        elif b == "-":
            answer = a - c
        elif b == "*":
            answer = a * c
        elif b == "/":
            answer = a / c
        elif b == "%":
            answer = a % c
        else:
            answr = "잘못된 연산자"
        return answer

if __name__ == "__main__":
    solution = Culcurator()
    a = int(input("첫번째 수 : "))
    b = input("연산자 : ")
    c = int(input("두번째 수 : "))
    print(solution.solution(a, b, c))