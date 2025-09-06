class Solution:
    def reverseString(self, s: 'List[str]') -> 'None':
        """
        Do not return anything, modify s in-place instead.
        """
        # // operator - floor division
        for i in range(len(s)//2):
            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]

            # same as above
            # tmp = s[i]
            # s[i] = s[len(s)-1-i]
            # s[len(s)-1-i] = tmp
            print(s)

 
solution = Solution()
s = ["h","e","l","l","o"]
print(solution.reverseString(s))
"""
0 1 2 3 4 5 6 7
2 4 1 6 0 3 4 6
"""