if __name__ == '__main__':
    N = int(input())

    myList =[]
    
    for i in range(N):
        function = input().strip().split()
        
        if function[0] == "insert":
            myList.insert(int(function[1]),int(function[2]))
        
        if function[0] == "remove":
            myList.remove(int(function[1]))
            
        if function[0] == "append":
            myList.append(int(function[1]))
            
        if function[0] == "sort":
            myList.sort()
            
        if function[0] == "pop":
            myList.pop()
            
        if function[0] == "reverse":
            myList.reverse()
            
        if function[0] == "print":
            print(myList)
        
