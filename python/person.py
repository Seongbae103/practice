from stat import SF_SNAPSHOT
from unicodedata import name


class Person:
    def __init__(self, name, ssn, addr):
        self.name = name
        self.ssn = ssn
        self.age = 0
        self.gender = ""
        self.addr = addr

    def gender_check(self):
        self.gender_checker = int(self.ssn[7])
        if self.gender_checker == 1 or self.gender_checker == 3:
            self.gender = "남자"
        elif self.gender_checker == 2 or self.gender_checker == 4:
            self.gender = "여자"
            
    def set_year(self):
        gender_checker = self.gender_checker
        self.yy = int(self.ssn[:2]) #:2는 생년
        if self.yy <= 22: 
            if gender_checker == 3 or gender_checker == 4:
                self.yy += 2000
        else:
            if gender_checker == 1 or gender_checker == 2:
                self.yy += 1900

    def set_age(self):
        current_year = 2022
        self.age = current_year - self.yy +1
    
    def print_person(self):
        print("### 자기소개 ###" 
            "\n ************************************" 
            f"\n 이름 : {self.name}" 
            f"\n 나이 : {self.age}"
            f"\n 성별 : {self.gender}"
            f"\n 주소 : {self.addr}"
            "\n ************************************")
        
    @staticmethod
    def main():
        name = input("이름 : ")
        ssn = input("주민번호 : ")
        addr = input("주소 : ")
        person = Person(name, ssn, addr)
        person.gender_check()
        person.set_year()
        person.set_age()
        person.print_person()
Person.main()