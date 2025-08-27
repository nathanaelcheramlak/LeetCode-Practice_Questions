class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat_count = 0
        left = 0
        right = len(people) - 1
        while right > left:
            if people[right] + people[left] <= limit:
                left += 1
            
            boat_count += 1
            right -= 1

        if right == left:
            return boat_count + 1

        return boat_count