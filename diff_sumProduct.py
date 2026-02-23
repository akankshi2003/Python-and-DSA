class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n!=0:
            prod=1
        else:
            return 0
        sm=0
        while n!=0:
            k=n%10
            prod*=k
            sm+=k
            n//=10
        return (prod-sm)

if __name__ == "__main__":
    obj = Solution()
    n = int(input("Enter number : "))
    print(obj.subtractProductAndSum(n))