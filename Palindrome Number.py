class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Convert the int into string and then reverse the string through index slicing [::-1]
        if str(x) == (str(x)[::-1]):
            return True
        else:
            return False
        
