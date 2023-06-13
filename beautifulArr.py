def setFunction():
 
    set_one = []  # zero set
    set_two = []  # positive set
    set_three = []  # negative set
 
    total_elements = int(input())
 
    elements = list(map(int, input().split()))
 
    elements.sort()
 
    if elements[-1] > 0:
        set_two.append(elements[-1])
        elements.pop()
 
        set_three.append(elements[0])
 
        set_one_start = 1
 
    else:
        set_two.append(elements[0])
        set_two.append(elements[1]) #solution always exsists, two negatives will make a postive product
 
        set_three.append(elements[2])
 
        set_one_start = 3
 
    set_one = elements[set_one_start:]
 
    print("1", set_three[-1])
 
    print(len(set_two), end=" ")
    print(*set_two)
 
    print(len(set_one), end=" ")
    print(*set_one)
 
 
setFunction()
