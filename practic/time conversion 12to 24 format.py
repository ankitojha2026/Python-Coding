def convert(time):
    l=time.split(':')
    hh=int(l[0])
    hht=''
    mm=l[1]
    temps=l[2]
    ss=temps[:2]
    period=temps[3:].upper()

    if period=='AM':
        if hh==12:
            hht='00'
        else:
             hht=str(hh)

    elif period=='PM':
        if hh!=12:
            hh+=12
            hht=str(hh)


#remove PM
    if period=='PM':
        return hht+":"+mm+":"+ss
    return hht+":"+mm+":"+ss+" AM
print(convert("01:00:00 AM"))
