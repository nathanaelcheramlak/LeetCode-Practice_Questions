class Solution:
    def convert(self, num):
        m = 10 ** (len(num) - 1)
        res = 0
        for n in num:
            res += int(n) * m
            m /= 10
        return int(res)
    def multiply(self, num1: str, num2: str) -> str:
        num1 = self.convert(num1)
        num2 = self.convert(num2)
        return f"{num1 * num2}"