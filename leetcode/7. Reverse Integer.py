class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        res = int('-' + s[1:][::-1]) if s[0] == '-' else int(s[::-1])
        print(res)
r = Solution()
r.reverse(123)