class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Bruteforce
        def find_max(candies):
            max_candy = candies[0]
            for candy in candies:
                max_candy = max(max_candy, candy)
            return max_candy
        
        max_candy = find_max(candies)
        output = []
        for candy in candies:
            if extraCandies + candy < max_candy:
                output.append(False)
            else:
                output.append(True)
        
        return output