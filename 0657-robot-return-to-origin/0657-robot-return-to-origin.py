class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count = Counter(moves)
        return count['U'] == count['D'] and count['R'] == count['L'] 