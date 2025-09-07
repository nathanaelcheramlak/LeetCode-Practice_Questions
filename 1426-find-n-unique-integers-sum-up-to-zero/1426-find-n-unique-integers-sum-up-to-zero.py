class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]

        arr = []
        for i in range(1, n):
            arr.append(i)

        arr.append(-sum(arr))
        return arr