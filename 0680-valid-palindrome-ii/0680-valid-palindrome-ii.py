class Solution:
    def validPalindrome(self, s: str) -> bool:
        shouldPass = True
        l = 0
        r = len(s) - 1
        while r >= l:
            print(f'Left: {l}, Right: {r}')
            print(f"[{s[l]}] vs [{s[r]}]")
            if s[l] != s[r] and not shouldPass:
                return False
            if s[l] != s[r]:
                mid = len(s) // 2
                print(f"[{s[l+1:mid+1]}] vs [{s[mid+1:r+1]}]")
                if s[l+1:mid+1] == s[mid+1:r+1][::-1]:
                    l += 1
                else:
                    r -= 1
                shouldPass = False
            else:
                r -= 1
                l += 1
        
        return True