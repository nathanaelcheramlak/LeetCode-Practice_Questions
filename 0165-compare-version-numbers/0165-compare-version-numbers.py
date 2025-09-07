class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split('.')
        ver2 = version2.split('.')
        v1 = len(ver1)
        v2 = len(ver2)
        for i in range(max(v1, v2)):
            one = 0
            if i < v1:
                one = int(ver1[i])
            two = 0
            if i < v2:
                two = int(ver2[i])
            if one > two:
                return 1
            if two > one:
                return -1
        
        return 0