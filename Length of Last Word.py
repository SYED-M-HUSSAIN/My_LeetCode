class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        var=s.strip() # remove the whitespaces from the start and end of the string
        var_list= (list(var[::-1])) # convert the string into list and reverse the order 
        length=0
        for x in var_list:
            if x == ' ':
                break
            else:
                length+=1
        return length
