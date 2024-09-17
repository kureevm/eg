for a in range(111):
    f=1
    for x in range(111):
        f *= (x & 39==0) or ((x & 11==0) <= (not(x & a==0 )))
    if f:
        print(a)
        