class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10==0 and x!=0):
            return False
        
        reverted_half = 0
        while x > reverted_half:
            reverted_half =(reverted_half * 10 + x % 10)
            x = x // 10 
        return x == reverted_half or x == reverted_half //10
        
if __name__ == "__main__":
    solution = Solution()
    test1= 121
    result= solution.isPalindrome(test1)
    print(f"Is {test1} palindrome? {result}")
    test2 = -121
    result2= solution.isPalindrome(test2)
    print(f"Is {test2} palindrome?\n {result2}")


