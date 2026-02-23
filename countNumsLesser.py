class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for i in nums:
            count = 0
            for j in nums:
                if j<i:
                    count+=1
            arr.append(count)
        return arr
if __name__ == "__main__":
    res = Solution()
    arr = []
    while True:
        x = int(input("Enter integers (To stop : enter -1) : "))
        if x == -1:
            break
        arr.append(x)
    output = res.smallerNumbersThanCurrent(arr)
    print(output)