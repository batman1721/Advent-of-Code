import matplotlib.pyplot as plt#part2

listax=[]#part2
listay=[]#part2

def dir_cord(d,val,lista):
    if d==1:
        lista[1]=lista[1]+val
        listax.append(lista[1])#part2
        listay.append(lista[0])#part2
    elif d==2:
        lista[0]=lista[0]+val
        listax.append(lista[1])#part2
        listay.append(lista[0])#part2
    elif d==3:
        lista[1]=lista[1]-val
        listax.append(lista[1])#part2
        listay.append(lista[0])#part2
    elif d==4:
        lista[0]=lista[0]-val
        listax.append(lista[1])#part2
        listay.append(lista[0])#part2
    return lista

def euc_dir(t,d):
        if d==1:
            if t=='R':
                d=2
            elif t=='L':
                d=4                
        elif d==2:
            if t=='R':
                d=3                
            elif t=='L':
                d=1                
        elif d==3:
            if t=='R':
                d=4                
            elif t=='L':
                d=2                
        elif d==4:
            if t=='R':
                d=1                
            elif t=='L':
                d=3
        return d

def taxicab_route(z):
    coord=[0,0]
    d=1
    z=z.replace(',','').split(' ')
    for i in xrange(0,len(z)):        
        d=euc_dir(z[i][0],d)
        dir_cord(d,int(z[i][1:]),coord)
    return coord

z='R1, R1, R3, R1, R1, L2, R5, L2, R5, R1, R4, L2, R3, L3, R4, L5, R4, R4, R1, L5, L4, R5, R3, L1, R4, R3, L2, L1, R3, L4, R3, L2, R5, R190, R3, R5, L5, L1, R54, L3, L4, L1, R4, R1, R3, L1, L1, R2, L2, R2, R5, L3, R4, R76, L3, R4, R191, R5, R5, L5, L4, L5, L3, R1, R3, R2, L2, L2, L4, L5, L4, R5, R4, R4, R2, R3, R4, L3, L2, R5, R3, L2, L1, R2, L3, R2, L1, L1, R1, L3, R5, L5, L1, L2, R5, R3, L3, R3, R5, R2, R5, R5, L5, L5, R2, L3, L5, L2, L1, R2, R2, L2, R2, L3, L2, R3, L5, R4, L4, L5, R3, L4, R1, R3, R2, R4, L2, L3, R2, L5, R5, R4, L2, R4, L1, L3, L1, L3, R1, R2, R1, L5, R5, R3, L3, L3, L2, R4, R2, L5, L1, L1, L5, L4, L1, L1, R1'
T=taxicab_route(z)

print abs(T[0])+abs(T[1])

#Part 2

plt.plot(listax,listay)
plt.show() #Visual answer, just zoom in
