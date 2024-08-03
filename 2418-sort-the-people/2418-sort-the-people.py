class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        maps = dict()
        names_sorted = []
        for i in range(len(heights)):
            key = heights[i]
            value = names[i]
            maps[key] = value
        heights.sort(reverse=True)
        
        for h in heights: 
            name = maps.get(h)
            names_sorted.append(name)
        return names_sorted
        
        