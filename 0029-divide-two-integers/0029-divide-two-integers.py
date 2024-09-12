class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        sign = 1 if (dividend * divisor) > 0 else -1

        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0

        # Using Exponential Search
        while dividend >= divisor:
            temp = divisor
            mul = 1
            while dividend >= temp:
                dividend -= temp
                result += mul

                mul += mul
                temp += temp

        result *= sign

        if result > MAX_INT:
            return MAX_INT
        if result < MIN_INT:
            return MIN_INT

        return result