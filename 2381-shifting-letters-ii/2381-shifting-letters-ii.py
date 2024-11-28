class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0] * len(s)
        for shift in shifts:
            for i in range(shift[0], shift[1] + 1):
                if shift[-1] == 0: # Shift Backward
                    arr[i] -= 1
                else: # Shift Forward
                    arr[i] += 1
        
        for i in range(len(arr)):
            ascii_code = ord(s[i]) + arr[i]
            val = chr((ascii_code - 97) % 26 + 97) # To make it circular.
            arr[i] = val
        
        return ''.join(arr)
            
