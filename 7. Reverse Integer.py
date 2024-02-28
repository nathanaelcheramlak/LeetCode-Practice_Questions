# Problem #7

"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], 
then return 0.
"""
def reverse(x):
    # To store the reversed integer
    reversed = 0

    while x != 0:
        lastDigit = x % 10
        reversed = 10 * reversed + lastDigit
        x //= 10
    if  reversed > 2147483647 or reversed < -2147483648:
        return 0
    return reversed

# Time Complexity: O(log(x)) -> Since the number of digits in x is proportional to the logarithm of x
# Space Complexity: O(1)