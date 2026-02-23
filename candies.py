class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        out = []
        max_candies = max(candies)
        for i in candies:
            out.append(i + extraCandies >= max_candies)
        return out
        # for i in candies:
        #     flag = 1
        #     for j in candies:
        #         if j==i:
        #             continue
        #         if (i + extraCandies) < j:
        #             flag = 0
        #     if flag == 1:
        #         out.append(True)
        #     else:
        #         out.append(False)
        # return out
if __name__ == "__main__":
    obj = Solution()
    i=0
    candies=[]
    while i!=-1:
        i = int(input(f"Enter number of candies child {i} (Enter -1 to stop)"))
        candies.append(i)
    extra = "Enter the number of extracandies : "
    print(obj.kidsWithCandies(candies, extra))  