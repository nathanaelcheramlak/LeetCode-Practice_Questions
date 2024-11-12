class Solution(object):
    def check(self, piles, speed):
        hour = 0
        for pile in piles:
            hour += (pile - 1) // speed + 1
        return hour

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        min_speed = 1
        max_speed = max(piles)
        while min_speed <= max_speed:
            avg = (max_speed + min_speed) // 2
            reqHr = self.check(piles, avg)
            if h >= reqHr:
                max_speed = avg - 1
            else:
                min_speed = avg + 1
        return min_speed