class Solution:
    # https://labuladong.github.io/algo/di-yi-zhan-da78c/shou-ba-sh-48c1d/shuang-zhi-fa4bd/
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            s1 = self.palindrome(s, i, i)
            s2 = self.palindrome(s, i, i+1)
            res = s1 if len(s1) > len(res) else res
            res = s2 if len(s2) > len(res) else res
        return res

    # 在 s 中寻找以 s[l] 和 s[r] 为中心的最长回文串
    def palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]


solution = Solution()
s = "bdrgrtffd"
print(solution.longestPalindrome(s))
