import random #generates random value
import shelve
with shelve.open('Ci',writeback=True) as db:
    r=db['random']
    cipher=db['cipher']
    Accname=db['Accname']
    key_pair=db['key_pair']
def deletion(loc): #deletes given position
    print(key_pair)
    print(cipher)
    changes=dict()
    print(loc)
    print(key_pair)
    del key_pair[loc]
    mask=cipher.pop(loc)
    print("The Deleted value is:",mask)
    for i in range(loc+1,len(key_pair)+6): #for loop to check other cipher contains location as dependancy
        var=key_pair[i]
        temp=list(key_pair[i].keys())
        if loc in var.values(): #alters the dependant ciphers
            temp1=list(key_pair[i].values())
            temp1 = [cipher[x] if x < loc else (mask if x == loc else cipher[x - 1]) for x in temp1]
            temp2=[r[x] for x in temp]
            lol=decryptor(temp2,temp1)
            changes.update({i-1:lol})    
        for j in temp: #reduces values >position by 1
             if var[j]>loc:
                 var[j]-=1           
    print("The values to be changed are:",changes)                    
    for i in range (loc+1,(len(key_pair)+6)): #reduces key >position by -1
        key_pair[i-1]=key_pair.pop(i)
    for key,value in changes.items():
            calculation(value,key)     
    print("The Updated Key-Pairs are:",key_pair)                           
    return 0
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
    print("The available Key pairs are:",key_pair)
        
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
def deletion2(name):
    with shelve.open('Ci',writeback=True) as db:
        r=db['random']
        cipher=db['cipher']
        Accname=db['Accname']
        key_pair=db['key_pair']
    print(Accname)
    loc = Accname[name]
    print(loc)
    for key, value in Accname.items():
        if value > loc:
            Accname[key] = value - 6
    print(Accname)        
    for pos in range(loc,loc+6):
        deletion(loc)
    del Accname[name]    
    with shelve.open('Ci',writeback=True) as db:       
        db['cipher'] = cipher
        db['Accname'] = Accname
        db['key_pair'] = key_pair
                