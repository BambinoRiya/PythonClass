def split_and_join(line):
    i = line.split()
    i = '-'.join(i)
    
    return i
    
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
