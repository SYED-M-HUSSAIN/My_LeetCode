class Solution:
    def reverseWords(self, s: str) -> str:
        l =list(s.strip())
        #print(len(l))
        li=[]
        c=0
        word = ""
        for x in l:
            if x == ' ':
                li.append(word)
                c+=1
                word=""
                #print("ss",c)
            else:
                if len(l)-1== c:
                    word+=x
                    li.append(word)
                    c+=1
                else:
                    c+=1
                    word +=x
                    #print(c)
        count =0
        for x in li:
            #print("ss",x)
            if x == '':
                count+=1
                # print(x)
                # li.remove(x)
        for x in range(count):
            li.remove('')
        mess=""
        for x in li[::-1]:
            mess+=x+" "
        return mess.strip()
