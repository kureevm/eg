s=open('24_7600.txt').readline()
s=s.replace('QQ', 'Q Q')
s=s.replace('RR', 'R R')
s=s.replace('SS', 'S S')
s=s.replace('QR', 'Q R')
s=s.replace('RQ', 'R Q')
s=s.replace('QS', 'Q S')
s=s.replace('SQ', 'S Q')
s=s.replace('RS', 'R S')
s=s.replace('SR', 'S R')
ma=0
for i in s.split():
    ma = max(ma,len(i))
print(ma)