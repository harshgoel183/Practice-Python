class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        S = set()
        if x < 0:
            return False
        x = str(x)

        for i in range(0, len(x) // 2):
            for j in range(len(x) - 1, len(x) // 2, -1):
                if x[i] != x[j]:
                    return False

        return True

R = Solution()
R.isPalindrome(10)