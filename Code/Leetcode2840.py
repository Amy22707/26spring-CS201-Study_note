class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s11,s12,s21,s22=[],[],[],[]
        n=len(s1)
        for i in range(n):
            if(i%2==0):
                s11.append(s1[i])
                s21.append(s2[i])
            else:
                s12.append(s1[i])
                s22.append(s2[i])
        s11.sort()
        s12.sort()
        s21.sort()
        s22.sort()
        if(s11==s21 and s12==s22):
            return True
        return False