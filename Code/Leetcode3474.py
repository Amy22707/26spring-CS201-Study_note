class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n=len(str1)
        m=len(str2)
        a=['?']*(n+m-1)
        for i in range(n):
            if(str1[i]=='T'):
                for j in range(i,i+m):
                    if(a[j]!='?' and a[j]!=str2[j-i]):
                        return ""
                    a[j]=str2[j-i]
        qaq=a.copy()
        for i in range(n+m-1):
            if(qaq[i]=='?'):
                qaq[i]='a'
        for i in range(n):
            if(str1[i]=='F'):
                if("".join(qaq[i:i+m])==str2):
                    for j in range(i+m-1,i-1,-1):
                        if('?' not in a[i:i+m]):
                            return ""
                        if(a[j]=="?"):
                            qaq[j]='b'
                            break
        return "".join(qaq)
print(Solution().generateString("TTFFT","fff"))