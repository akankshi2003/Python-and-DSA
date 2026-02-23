class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        return ((high + 1) // 2) - (low // 2)
if __name__=="__main__":
    count=Solution()
    low = int(input("Give the lower number of the interval : "))
    high = int(input("Give the higher number of the interval : "))
    output = count.countOdds(low, high)
    print(output)