class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(0,len(nums)):
        #     temp = nums[i]
        #     for j in range(i+1,len(nums)):
        #         if (temp + nums[j]) == target:
        #             return ([i, j])
        diction = {}
        for i in range(0, len(nums)):
            valv = target - nums[i]
            if (target - valv) in diction:
                return (diction.get(target - valv), i)
            else:
                diction[valv] = i

s = Solution()
print(s.twoSum([3,2,4],6))

