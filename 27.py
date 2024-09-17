s= open('27A_7603.txt')
n = s.readline()
k = int(s.readline())
s= [int(x) for x in s]
ma=0
for i in range(len(s)-k):
    a=s[i]
    b = a+max(s[i+k:])
    ma=max(b,ma)
print(ma)