#Day 5: How About a Nice Game of Chess?

import hashlib

angela=[]
m=''
i=0
while len(angela)<=7:
    code='ugkcyxxp'+str(i)
    code=code.encode('utf-8')
    i=i+1
    m=hashlib.md5()
    m.update(code)
    m=m.hexdigest()
    if str(m)[:5]=='00000':
        angela.append(m[5])
        print (angela)
