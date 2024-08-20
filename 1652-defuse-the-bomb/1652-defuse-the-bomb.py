class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        N = len(code)
        decrypted = [0] * len(code)
        if k == 0:
            return decrypted
        for i in range(N):
            if k > 0:
                total = 0
                for item in range(1, k+1):
                    total += code[(i + item) % N]
                decrypted[i] = total
            else:
                total = 0
                for item in range(1, -k+1):
                    total += code[(i - item) % N]
                decrypted[i] = total
        return decrypted