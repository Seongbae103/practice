class Grade(object):
    def __init__(self, name, ko, en, ma):
        self.name = name
        self.ko = ko
        self.en = en
        self.ma = ma
        self.set_total()
        self.set_avg()
        self.set_grade()

    def set_total(self):
        self.total = self.ko + self.en + self.ma

    def set_avg(self):
        self.avg = self.total / 3

    def set_grade(self):
        avg = self.avg
        if avg >= 90: grade = "A"
        elif avg >= 80: grade = "B"
        elif avg >= 70: grade = "C"
        elif avg >= 60: grade = "D"
        elif avg >= 50: grade = "E"
        else : grade = "F"
        self.grade = grade 

    def print_grade(self):
        print(f"{self.name} {self.ko} {self.en} {self.ma} {self.total} {self.avg} {self.grade}")

    @staticmethod
    def new_grade():
        return Grade(input("이름 : "),
                    int(input("국어 : ")),
                    int(input("영어 : ")),
                    int(input("수학 : ")))

    @staticmethod
    def print_result(ls):
        print("### GRADE ###")
        print("*********************************")
        print("이름 국어 영어 수학 총점 평균 등급")
        print("*********************************")
        [i.print_grade() for i in ls]
        print("*********************************")    
    
    @staticmethod
    def print_menu():
        print("1. 성적 입력")
        print("2. 성적 출력")
        print("3. 성적 삭제")
        print("4. 종료 ")
        return int(input("실행 : "))

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Grade.print_menu()
            if menu == 1:
                print(" ## 성적 입력 ##")
                ls.append(Grade.new_grade())
            elif menu == 2:
                print(" ## 성적 출력 ##")
                Grade.print_result(ls)
            elif menu == 3:
                print(" ## 성적 삭제 ##")
            elif menu == 4:
                print(" ## 종료 ## ")
                break

Grade.main()