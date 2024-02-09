class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        ans=""
        for x in digits:
            s+=str(x)
        ans+= str(int(s)+1)
        x = [int(i) for i in ans]
        return x
