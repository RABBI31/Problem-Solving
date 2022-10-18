class Solution(object):
    def hammingDistance(self, x, y):
        return sum([int(b) for b in "{:b}".format(x^y)])
        
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        