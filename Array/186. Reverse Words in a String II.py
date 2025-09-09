from typing import List

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # Helper: reverse subarray [l, r]
        def reverse(l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l, r = l + 1, r - 1

        n = len(s)
        # Step 1: reverse the whole list
        reverse(0, n - 1)

        # Step 2: reverse each word
        start = 0
        for i in range(n + 1):
            if i == n or s[i] == ' ':
                reverse(start, i - 1)
                start = i + 1


s = list("the sky is blue")
print(s)
Solution().reverseWords(s)
print("".join(s))   # 输出: "blue is sky the"