class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        1, 11, 21, 1211, 111221, ...312211
        """
        x = "1";
        stri = "";
        if n <= 1:
            return "1";
        stri = x;
        while(n != 1):
            n = n - 1;
            stri = str(len(stri)) + stri;
        return stri;
p = Solution();
print(p.countAndSay(2));