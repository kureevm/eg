s= [int(x) for x in open('17_7596.txt')]
mi=10000000000000000
h=[]
for i in s:
    if i%10==5:
        mi=min(mi,i)
for i in range(len(s)-1):
    a=s[i]
    b=s[i+1]
    if ((len(str(a))==3 and len(str(b))!=3) or (len(str(a))!=3 and len(str(b))==3)) and (a+b)%mi==0:
        h.append(a+b)
print(len(h),min(h))