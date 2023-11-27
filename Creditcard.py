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
# name=input("The Name to Decipher:")
# loc=Accname[name]
# for de in range(loc,loc+6):
#     temp,temp1=[r[x] for x in list(key_pair[de].keys())],[cipher[x] for x in list(key_pair[de].values())]
#     nws=decryptor(temp,temp1)
#     if cipher[loc]==nws:
#         continue
#     else:
#         flag=1
# if flag==0:
#     print("Deducted")
# else:            
#     print("Not deducted")