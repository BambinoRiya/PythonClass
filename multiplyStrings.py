class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        multiply = lambda x, y: int(x) * int(y)
        return str(multiply(num1, num2))
