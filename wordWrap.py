import textwrap

def wrap(string, max_width):
    newList = []
    i=0
    j= max_width
    
    while j < len(string):
        sliced_str = string[i:j] 
        
        i = i + max_width
        j = j + max_width
        
        newList.append(sliced_str)
        
        if j > len(string):
            newList.append(string[i:]) #prints out from i to the end 
        
    answer = '\n'.join(newList)
    return answer

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
