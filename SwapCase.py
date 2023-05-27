def swap_case(s):
    newString = ""
    #to_array = list(s)
    for char in s:
        if char.isupper():
            newString += char.lower()
        elif char.islower():
            newString += char.upper()
        else:
            newString += char #for characters like numbers and other special characters
    
    return newString     

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
