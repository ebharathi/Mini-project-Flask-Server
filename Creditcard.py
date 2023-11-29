plain=[]
flag=0
import random #generates random value
import shelve
with shelve.open('Ci') as db:
    r=db['random']
    cipher=db['cipher']
    Accname=db['Accname']
    key_pair=db['key_pair']
def decryptor(n,m): #code to decrypt
    t=[m[i]+n[i] for i in range(len(m)-1)]
    t.append(m[(len(m)-1)]+n[(len(m)-1)])
    q=(t[0]^t[1])
    for i in range(len(m)-2):
        q=(q^t[2+i])
    return(q)
