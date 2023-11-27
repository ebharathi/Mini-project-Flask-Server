import random #generates random value
import shelve
with shelve.open('Ci') as db:
    r=db['random']
    cipher=db['cipher']
    Accname=db['Accname']
    key_pair=db['key_pair']
def encryptop(x,y,n,pos): #encrypts based on index
    dict={y[i]:x[i] for i in range(2)}
    a,b=[],[]
    for i in dict.keys():
        a.append(r[i])
    for i in dict.values():
        b.append(cipher[i])  
    a.append(r[y[2]])
    t=[b[i]+a[i] for i in range(2)]
    s=(t[0]^t[1])
    new_cipher=(n^s) 
    new_cipher=round(new_cipher-a[2]) #caluclated new cipher    
    dict.update({y[2]:pos})
    print("The key is :",dict)
    if (pos<len(cipher)): #updates or appends cipher based on existense
        cipher[pos]=new_cipher    
    else :     
        cipher.append(new_cipher)   
    key_pair.update({pos:(dict)})
def calculation(n,pos): #code to encrypt
    x=random.sample(range(0,pos-1),2) 
    y=random.sample(range(0,len(r)-1),3) 
    encryptop(x,y,n,pos)    
    print("Updated Cipher:",cipher,"\nSuccessfully inserted")
def decryptor(n,m): #code to decrypt
    t=[m[i]+n[i] for i in range(len(m)-1)]
    t.append(m[(len(m)-1)]+n[(len(m)-1)])
    q=(t[0]^t[1])
    for i in range(len(m)-2):
        q=(q^t[2+i])
    return(q)
def updation(pos,temp,temp1): #updates cipher with new random and key values
    y=temp
    x=temp1
    mask=cipher[pos]
    temp,temp1=[r[x] for x in list(key_pair[pos].keys())],[cipher[x] for x in list(key_pair[pos].values())]
    n=decryptor(temp,temp1)
    encryptop(x,y,n,pos)
    print("Updated cipher:",cipher[pos])
    for i in range(pos+1,len(cipher)): #for loop to check other cipher contains location as dependancy
        x,y=list(key_pair[i].values()),list(key_pair[i].keys())
        if pos in x: #alters the dependant ciphers
            temp1=[mask if x==pos else cipher[x] for x in list(key_pair[i].values())]
            temp=[r[x] for x in list(key_pair[i].keys())]
            ans=decryptor(temp,temp1)
            encryptop(x,y,ans,i)
    with shelve.open('Ci') as db:
        db['cipher']=cipher
        db['Accname']=Accname
        db['key_pair']=key_pair