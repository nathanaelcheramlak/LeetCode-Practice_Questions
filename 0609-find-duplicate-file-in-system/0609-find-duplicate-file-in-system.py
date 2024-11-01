class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        map = dict()
        res = []
        for path in paths:
            files = path.split(' ')
            parent = files[0]
            for file in files[1:]:
                temp = file.split('(')
                content = (temp[1])[:-1]
                if content in map:
                    map[content].append(parent + "/" + temp[0]) 
                else:
                    map[content] = [parent + "/" + temp[0]]
        
        for val in map.values():
            if len(val) > 1:
                res.append(val)
        return res
