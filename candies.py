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
    while True:
        x = int(input("Enter integers (To stop : enter -1) : "))
        if x == -1:
            break
        candies.append(i)
    extra = int(input("Enter the number of extracandies : "))
    print(obj.kidsWithCandies(candies, extra))  