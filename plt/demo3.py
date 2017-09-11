import os

xdict = {}

with open('e:/crop/ocrRes.txt', 'r') as fp:
    for line in fp.readlines():
        xname, xsize, xtime, xstatus = line.split('\t')
        xpath, xfile = os.path.split(xname)
        hour, minute, second = xtime.split(':')
        if xpath in xdict:
            yytim = xdict.get(xpath)
            yytim = yytim + float(hour) * 3600 + float(minute) * 60 + float(second)
            xdict[xpath] = yytim
        else:
            xdict[xpath] = float(hour) * 3600 + float(minute) * 60 + float(second)

with open('e:/crop/new.txt', 'a') as ff:
    with open('e:/crop/handleRes.txt', 'r') as fp:
        for line in fp.readlines():
            xname, xsize, xtime, xstatus = line.split('\t')
            xpath, xtext = os.path.splitext(xname)
            hour, minute, second = xtime.split(':')
            xxtime = float(hour) * 3600 + float(minute) * 60 + float(second)
            if xpath in xdict:
                ytime = xxtime + xdict.get(xpath)
                yyti = '%.2f' % ytime
                ff.write(xpath + xtext + '\t' + xsize + '\t' + str(yyti) + '\t' + xstatus)
