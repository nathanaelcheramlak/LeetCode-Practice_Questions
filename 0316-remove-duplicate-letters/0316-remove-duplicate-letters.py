class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = {}
        for i, l in enumerate(s):
            count[l] = i

        stack = []
        unique = set()
        for i, let in enumerate(s):
            while stack and stack[-1] > let and count[stack[-1]] > i and let not in unique:
                l = stack.pop()
                unique.discard(l)
            if let not in unique:
                stack.append(let)
                unique.add(let)

        
        return ''.join(stack)




