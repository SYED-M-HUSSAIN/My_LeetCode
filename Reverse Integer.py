class Solution:
    def reverse(self, y: int) -> int:
        x = list(str(y))
        sign=""
        if x[0].isdigit() == False:
            sign = x[0]
            x.remove(sign)
        for y in x:
            if x[-1] == '0' and len(x)!=1:
                x.pop()
        for i in x[::-1]:
            sign+=i
        if (-2**31 > int(sign))  or (((2**31)-1)<int(sign)): 
            return 0
        else:
            return int(sign)
        
