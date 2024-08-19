class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        my_bills = {5: 0, 10: 0, 20: 0}  # We start with no cash
        for bill in bills:
            my_bills[bill] += 1
            
            if bill == 10:
                if my_bills[5] < 1:
                    return False
                my_bills[5] -= 1  # $5 change
            
            elif bill == 20:
                if my_bills[10] > 0 and my_bills[5] > 0:
                    # $10 and one $5
                    my_bills[10] -= 1
                    my_bills[5] -= 1
                elif my_bills[5] >= 3:
                    # Three $5 bills
                    my_bills[5] -= 3
                else:
                    return False  # Not enough change available
        
        return True
        # Time Complexity: O(n)
        # Space Complexity: O(1)
