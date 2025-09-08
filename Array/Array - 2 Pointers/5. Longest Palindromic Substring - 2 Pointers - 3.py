class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s

        start, end = 0, 0  # inclusive indices for the best window

        def expand(l: int, r: int) -> tuple[int, int]:
            # Expand while s[l..r] is a palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # After the loop, s[l+1..r-1] is the palindrome
            return l + 1, r - 1

        for i in range(len(s)):
            # Odd-length center at i
            l1, r1 = expand(i, i)
            # Even-length center at i, i+1
            l2, r2 = expand(i, i + 1)

            # Choose the longer one
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start : end + 1]