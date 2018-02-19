class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # print(bin(y)[2:].zfill(4),bin(x)[2:].zfill(4))
        # return(len(((bin(x ^ y))[2:]).split('0')))
        return bin(x ^ y).count('1')
        # r = bin(y)[2:].zfill(4)
        # s = bin(x)[2:].zfill(4)
        # print(r|s)

r = Solution()
print(r.hammingDistance(1, 4))