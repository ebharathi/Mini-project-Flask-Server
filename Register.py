import random #generates random value
import shelve
def encryptop(Accname,x,y,n,pos): #encrypts based on index
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
    print(cipher)
def calculation(n,pos): #code to encrypt
    with shelve.open('Ci') as db:
        r=db['random']
        cipher=db['cipher']
        Accname=db['Accname']
        key_pair=db['key_pair']
    x=random.sample(range(0,pos-1),2) 
    y=random.sample(range(0,len(r)-1),3) 
    encryptop(x,y,n,pos)       
    with shelve.open('Ci') as db:
        db['cipher']=cipher
        db['Accname']=Accname
        db['key_pair']=key_pair
    db.close()