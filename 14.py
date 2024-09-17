for x in '0123456789ABCDE':
    w = int('97968'+x+'13',15) + int('7'+x+'213',15)
    if w%14==0:
        print(w//14)
        break
    