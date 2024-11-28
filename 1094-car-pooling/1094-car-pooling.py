class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        distance = 0
        for c, f, t in trips:
            distance = max(distance, t)

        arr = [0] * (distance + 2)
        for num, f, t in trips:
            arr[f] += num
            arr[t] -= num

        # Prefix summer
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]
            if arr[i] > capacity:
                return False
        
        return True