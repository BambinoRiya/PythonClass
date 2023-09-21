def reverse(self, left, right):
        if left >= right:
            return 
        
        s[left], s[right] = s[right], s[left]
        reverse(self, left+1, right-1)
        
    reverse(self, 0, len(s)-1)
    
