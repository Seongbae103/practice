import random
class Bubb:
    def solution(self):
        title = "###버블정렬###"
        count = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th']
        dc = {}
        for i in count:
            dc[i]= random.randint(1, 10)
        for k,v in dc.items():
            print(f'{k} : {v}')
        if dc[i] == dc[i+1]:
            dc[i-1] = dc[i+1]


if __name__ == "__main__":
    solution = Bubb() 
    print(solution.solution()) 