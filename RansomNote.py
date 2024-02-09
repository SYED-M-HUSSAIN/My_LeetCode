class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1={}
        d2={}
        l1=list(magazine)
        l2=list(ransomNote)
        for x in l1:
            if x not in d1:
                d1[x]=1
            else:
                d1[x]+=1
        for y in l2:
            if y not in d2:
                d2[y]=1
            else:
                d2[y]+=1
        for x in ransomNote:
            if x in d1:
                if d1[x] >= d2[x]:
                    continue
                else:
                    return False
            else:
                return False
                
        return True
