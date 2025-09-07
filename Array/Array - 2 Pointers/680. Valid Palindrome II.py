class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Helper: check palindrome in s[i..j]
        def is_pal(i: int, j: int) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # One deletion allowed: skip left or skip right
                return is_pal(l + 1, r) or is_pal(l, r - 1)
        return True