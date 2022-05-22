import time

class Solution:
    ## We reverse half the number and compare with other half
    def isPalindrome(self, x: int) -> bool:
        # If x is a negative number it is not a palindrome
        # If x % 10 = 0, in order for it to be a palindrome the first digit should also be 0
        if x < 0 or (x > 0 and x%10 == 0):
            return False

        reversedNum = 0
        
        '''
        when reversedNum is equal (for even palindromes) or bigger (for odd) it means that we've reached or passed the middle point
        '''
        while x > reversedNum:
            reversedNum = reversedNum * 10 + x % 10
            x = x // 10

        # If x is equal to reversed number then it is a palindrome
        # If x has odd number of digits, dicard the middle digit before comparing with x
        # Example, if x = 23132, at the end of for loop x = 23 and reversedNum = 231
        # So, reversedNum/10 = 23, which is equal to x
        return (
            x == reversedNum or                    # even numbers
            x == reversedNum // 10                 # odd numbers
        )


# Program
s1 = 121
s2 = -121
s3 = 10

t0 = time.perf_counter_ns()

s = Solution()

print(s.isPalindrome(s1))
print(s.isPalindrome(s2))
print(s.isPalindrome(s3))

t1 = time.perf_counter_ns()

print(f"{(t1 - t0) / 1000000} ms.")