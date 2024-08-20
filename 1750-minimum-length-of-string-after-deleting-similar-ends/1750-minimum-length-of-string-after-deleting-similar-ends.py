class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = len(s) - 1

        while right > left and s[left] == s[right]:
            current_letter = s[left]

            # Move left pointer forward if it matches current_letter
            while left <= right and s[left] == current_letter:
                left += 1

            # Move right pointer backward if it matches current_letter
            while left <= right and s[right] == current_letter:
                right -= 1

        # Return the length of the remaining substring
        return right - left + 1


