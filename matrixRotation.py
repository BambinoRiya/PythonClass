def rotate(mat):
    mat[0][0],mat[0][1] = mat[0][1], mat[0][0]
    mat[1][0],mat[1][1] = mat[1][1], mat[1][0]
    mat[0][0], mat[1][1] = mat[1][1], mat[0][0]
    return mat

def isPretty(matrix):
    if matrix[0][0] < matrix[0][1] and matrix[1][0] < matrix[1][1] and matrix[0][0] < matrix[1][0] and matrix[0][1] < matrix[1][1]:
        return True

def solve():
    res = []
    arr1 = list(map(int, input().split()))
    arr2= list(map(int, input().split()))
    res.append(arr1)
    res.append(arr2)  
        
        
    for _ in range(4):    
        if isPretty(res):
            return "YES"
        res = rotate(res)
    return "NO"

t = int(input())
for _ in range(t):
    print(solve())
