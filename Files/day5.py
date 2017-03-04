#Day 5: How About a Nice Game of Chess?

import hashlib

angela=[]
m=''
i=0

#Parte 1
##while len(angela)<=7:
##    code='ugkcyxxp'+str(i)
##    code=code.encode('utf-8')
##    i=i+1
##    m=hashlib.md5()
##    m.update(code)
##    m=m.hexdigest()
##    if str(m)[:5]=='00000':
##        angela.append(m[5])
##        print (angela)

#Parte 2
angela1=['','','','','','','','']
p=0
while p<=7:
    code='ugkcyxxp'+str(i)   
    code=code.encode('utf-8')
    i=i+1
    m=hashlib.md5()
    m.update(code)
    m=m.hexdigest()
    if str(m)[:5]=='00000' and (str(m)[5]).isnumeric()==True and int(str(m)[5])<=7:
        u=int(str(m)[5])
        if angela1[u]=='':
            angela1[u]=str(m)[6]
        print (angela1)
