class Solution(object):
    def countPrimes(self, n):
       
        prime_numbers = 0

        def isPrime(i):
            for x in range(2,i):
               if i%x == 0:
                    return False
            return True
                

        for z in range(2,n):
            if isPrime(z):
                prime_numbers +=1  
        return prime_numbers   
