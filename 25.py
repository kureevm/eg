s= ['']+ list('0123456789')
for s1 in s:
    for s2 in '0123456789':
        for s3 in '0123456789':
            w = '12'+s2+s3+'36'+s1+'1'
            w=int(w)
            if w %273==0:
                print(w,w//273)