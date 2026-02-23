class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = num
        count = 0
        while i!=0:
            k=i%10
            if num%k==0:
                count +=1 
            i//=10
        return count
    
if __name__ == "__main__":
    obj = Solution()
    n = int(input("Enter the number : "))
    result = obj.countDigits(n)
    print(result)