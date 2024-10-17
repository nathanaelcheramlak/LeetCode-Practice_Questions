class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def minPosition(arr, target):
            left = 0
            right = len(arr) - 1
            mid = 0
            while right >= left:
                mid = (left + right) // 2
                if arr[mid] > target:
                    right = mid - 1
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    return mid
            if arr[mid] < target:
                return mid + 1
            return mid
        
        idx = minPosition(arr, x)
        print("idx", idx)
        output = [arr[idx]]
        r = idx
        l = idx
        while len(output) < k:
            if arr[l-1] and abs(x - arr[l - 1]) <= abs(x - arr[r + 1]):
                l -= 1
                output.append(arr[l])
                
                print("Left Added")
            if arr[r+1] and abs(x - arr[l - 1]) > abs(x - arr[r + 1]):
                r += 1
                output.append(arr[r])
                
            print(output)
        output.sort()
        return output  