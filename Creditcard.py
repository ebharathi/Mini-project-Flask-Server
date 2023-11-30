import random #generates random value
import shelve
with shelve.open('Ci') as db:
    r=db['random']
    cipher=db['cipher']
    Accname=db['Accname']
    key_pair=db['key_pair']
def decryptor(n,m,): #code to decrypt
    t=[m[i]+n[i] for i in range(len(m)-1)]
    t.append(m[(len(m)-1)]+n[(len(m)-1)])
    q=(t[0]^t[1])
    for i in range(len(m)-2):
        q=(q^t[2+i])
    return(q)
def decryption2(name,message):  
    flag=0
    print(Accname)
    print("--->",name) 
    print(message)
    loc=Accname[name]
    print(int(loc))
    for de in range(0,6):
        print(message[de])
        temp,temp1=[r[x] for x in list(key_pair[loc+de].keys())],[cipher[x] for x in list(key_pair[loc+de].values())]
        nws=decryptor(temp,temp1)
        print(nws)
        print(flag)
        if nws==message[de]:
            print("succeded")
            continue
        else:
            flag=1
    if flag==0:
        print("Deducted")
    else:            
        print("Not deducted")       
