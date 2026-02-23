class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        rev = 0
        while temp>0:
            r = temp%10
            temp//=10
            rev = rev*10+r

        return rev==x
    
if __name__ == "__main__":
    obj = Solution()
    n = int(input("Enter number to check palindrome : "))
    print(obj.isPalindrome(n))