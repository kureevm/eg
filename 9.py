s =open('09_7588 (1).csv')
g=0
for i in s:
    h = sorted([int(x) for x in i.split(',')])
    hh=set()
    for i in h:
        hh.add(i)
    if len(hh)==5:
        if 3*(h[0]+h[4])<= sum(h[1:-1])*2:
            g+=1
print(g)