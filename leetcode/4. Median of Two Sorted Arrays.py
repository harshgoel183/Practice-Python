class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a = nums1 + nums2
        a.sort()
        length = len(a)
        if length % 2 == 0:
            return (float(a[length/2] + a[(length/2)-1]))/float(2)
            #return float((a[length/2] + a[(length/2)-1])/2)
        else:
            return a[length/2]
#*********************************************************************************************#