class Solution:
    def maximum69Number (self, num: int) -> int:
        temp = num
        to_add = 0
        position = 1
        while temp:
            digit = temp % 10
            temp //= 10
            if digit == 6:
                to_add = 3 * position 
            position *= 10

        return num + to_add