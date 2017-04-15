#Day 16 - Dragon Checksum

def bin_trans(x):
    y=x
    y=y[::-1]
    ytemp=''
    for i in xrange(len(y)):
        if y[i]=='0':
            ytemp+='1'
        elif y[i]=='1':
            ytemp+='0'
    y=ytemp
    return y

def res_data(x):
    return x+'0'+bin_trans(x)

def iter_res_data(x,y):
    p=x
    VARS=False
    while VARS==False:
        k=res_data(p)
        if len(k)>=y:
            break
        else:
            p=k
    k=k[:y]
    return k

def check(x):
    ans=''
    for i in xrange(0,len(x),2):
        if x[i]==x[i+1]:
            ans+='1'
        else:
            ans+='0'
    return ans

def iter_check(x):
    VARS=False
    p=x
    while VARS==False:
        y=check(p)
        if len(y)%2!=0:
            break
        else:
            p=y
    return y

code='10001001100000001'
length=35651584

print iter_check(iter_res_data(code,length))

