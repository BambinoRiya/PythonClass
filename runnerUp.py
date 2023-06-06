if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    newList = []
    biggestNum = max(arr)
    
    for index in arr:
        if index < biggestNum:
            newList.append(index)
            
    runnerUp = max(newList)
    
    print(runnerUp)
