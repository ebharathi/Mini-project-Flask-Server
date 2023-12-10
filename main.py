from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
# from schemas import Item
from fastapi.middleware.cors import CORSMiddleware
import random 
import shelve
# //importing function 
from Register import calculation2
from Delete import deletion2
from Update import updation
from Creditcard import decryption2
# USE THIS CODE TO CHECK THE VALUES IN DB 
with shelve.open('Ci',writeback=True) as db:
    r=db['random']
    cipher=db['cipher']
    Accname=db['Accname']
    key_pair=db['key_pair']
print("Random -> ",r)
print("cipher ->",cipher)
print("Accname->",Accname)
print("Key pair->",key_pair)
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
# get router 
@app.get("/")
def read_root():
    return {"Hello": "World"}
# to fetch db 
@app.get("/admin/db")
def get_db():
    with shelve.open('Ci') as db:
        r=db['random']
        cipher=db['cipher']
        Accname=db['Accname']
        key_pair=db['key_pair']
    print("DB SENT[+]")
    return {
        "cipher":cipher,
        "Accname":Accname,
        "key_pair":key_pair
    }
# to update DB
@app.post("/admin/db/update")
def update_db(item:dict):
       with shelve.open('Ci',writeback=True) as db:
            db['cipher'] = item["cipher"]
            db['Accname'] = item["Accname"]
            db['key_pair'] = item["key_pair"]
       print("DATABASE UPDATED[+]")
       print("new cipher--->",item["cipher"])
       print("new accname--->",item["Accname"])
       print("new key_pair--->",item["key_pair"])
       return {"error":"false"}
# post router for register
@app.post("/admin/register")
def register(item:dict):
    calculation2(item['name'],item['message'])
    return {"error":"false"}   
# Delete router 
@app.post("/admin/delete")
def delete(item:dict):
    deletion2(item['name'])
    return {"error":"false"}
# Update router 
@app.post("/admin/update")
def update(item:dict):
    name=item["name"]
    value=item["index"]   
    temp=item["temp"]
    temp1=item["temp1"]
    updation(name,value,temp,temp1)    
    # print("Updated Cipher:",cipher,"\nSuccessfully Updated")     
    return {"error":"false"}
#credit card router  
@app.post("/user/creditcard")
def creditcard(item:dict):
        return decryption2(item['name'],item['message'])
             

