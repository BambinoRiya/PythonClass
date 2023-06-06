if __name__ == '__main__':
    num = int(input()) #number of students in class
    students = {} #creating a dict for easier access of each element

    for _ in range(num):
        name = input()
        score = float(input())

        students[name] = score #adding each name and score to dict
        
    scores = set(students.values())
    second_lowest_score = sorted(scores)[1]

    
    names = [name for name, score in students.items() if score == second_lowest_score]
    names.sort()

    for name in names:
        print(name)
