import random #generates random value
import shelve
with shelve.open('Ci',writeback=True) as db:
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
    # print("The key is :",dict)
    if (pos<len(cipher)): #updates or appends cipher based on existense
        cipher[pos]=new_cipher    
    else :     
        cipher.append(new_cipher)   
    key_pair.update({pos:(dict)})
    # print(cipher)
def calculation(n,pos): #code to encrypt
    x=random.sample(range(0,pos-1),2) 
    y=random.sample(range(0,len(r)-1),3) 
    encryptop(x,y,n,pos)       
def calculation2(name, values):
    if len(Accname) == 0:
        counter = 0
    else:
        counter = len(Accname)
    Accname.update({name: 5 + (counter * 6)})
    counter += 1
    for i in values:
        calculation(int(i), len(cipher))
    with shelve.open('Ci', writeback=True) as db:
        db['cipher'] = cipher
        db['Accname'] = Accname
        db['key_pair'] = key_pair
    print("KEY VALUE PAIR:")
    print(key_pair)    
    print("UPDATED ACCOUNTS:")
    print(Accname)
    # db.close()
