import random #generates random value
import shelve

def decryptor(n,m,r,cipher,Accname,key_pair): #code to decrypt
    t=[m[i]+n[i] for i in range(len(m)-1)]
    t.append(m[(len(m)-1)]+n[(len(m)-1)])
    q=(t[0]^t[1])
    for i in range(len(m)-2):
        q=(q^t[2+i])
    return(q)
def decryption2(name,message):  
    try:
        with shelve.open('Ci') as db:
            r=db['random']
            cipher=db['cipher']
            Accname=db['Accname']
            key_pair=db['key_pair']
        flag=0
        print(Accname)
        print("--->",name) 
        print(message)
        loc=Accname[name]
        print(int(loc))
        for de in range(0,6):          
            if cipher[loc+de]==message[de]:
                print("Match: ",cipher[loc+de]," == ",message[de])
                
                continue
            else:
                print("Mismatch: ",cipher[loc+de]," != ",message[de])
                flag=1
        if flag==0:
            return {"error":"false"}
        else:            
            return {"error":"true"}
    except Exception as e:
        return {"error":"true"}
