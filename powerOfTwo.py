class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n%2==0:
            n//=2
        return n==1
if __name__ == "__main__":
    obj = Solution()
    n = int(input("Enter the number : "))
    result = obj.isPowerOfTwo(n)
    print(result)
    