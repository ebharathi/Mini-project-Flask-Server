from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
# from schemas import Item
from fastapi.middleware.cors import CORSMiddleware
import random 
import shelve
# //importing function 
from Register import calculation
from Delete import deletion
from Update import updation
from Creditcard import decryptor
with shelve.open('Ci') as db:
    r=db['random']
    cipher=db['cipher']
    Accname=db['Accname']
    key_pair=db['key_pair']
    
# creating app     
app = FastAPI()
# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# MONGODB CONNECTION
print("-----") 
# print(r)
# print(cipher)
# print(Accname)
# print(key_pair)
# MongoDB Connection Settings
# MONGO_URI = "mongodb+srv://projectone:projectone@cluster0.dzrb8.mongodb.net/?retryWrites=true&w=majority"
# client = AsyncIOMotorClient(MONGO_URI)
# print(client)
# database = client["miniproject"]
# collection = database["cipher"] 
# get router 
@app.get("/")
def read_root():
    return {"Hello": "World"}
# post router for register
@app.post("/admin/register")
def register(item:dict):
    with shelve.open('Ci') as db:
        r=db['random']
        cipher=db['cipher']
        Accname=db['Accname']
        key_pair=db['key_pair']
    if len(Accname)==0:
     counter=0
    else:
     counter=len(Accname)   
    print(item)
    name=item["name"]
    Accname.update({name:5+(counter*4)})
    counter+=1
    print(Accname)
    db.close()
    for i in item["message_array"]:
        calculation(int(i),len(cipher)) 
    return {"error":"false"}   
# Delete router 
@app.post("/admin/delete")
def delete(item:dict):
    with shelve.open('Ci') as db:
        r=db['random']
        cipher=db['cipher']
        Accname=db['Accname']
        key_pair=db['key_pair']
    name=item["name"]
    print(Accname)
    loc = Accname[name]
    print(loc)
    for key, value in Accname.items():
        if value > loc:
            Accname[key] = value - 6
    print(Accname)        
    for pos in range(loc,loc+7):
        deletion(loc)
    return {"error":"false"}
# Update router 
@app.post("/admin/update")
def update(item:dict):
    name=item["name"]
    value=item["index"]   
    temp=item["temp"]
    temp1=item["temp1"]
    pos=Accname[name]
    pos+=value
    updation(pos,temp,temp1)    
    print("Updated Cipher:",cipher,"\nSuccessfully Updated")     
    return {"error":"false"}
#credit card router  
@app.post("/user/creditcard")
def creditcard(item:dict):
        name=item["name"]
        loc=Accname[name]
        for de in range(loc,loc+6):
            temp,temp1=[r[x] for x in list(key_pair[de].keys())],[cipher[x] for x in list(key_pair[de].values())]
            nws=decryptor(temp,temp1)
            if cipher[loc]==nws:
                continue
            else:
                flag=1
        if flag==0:
            print("Deducted")
        else:            
            print("Not deducted")         

