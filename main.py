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
    decryption2(item['name'],item['message'])
        # name=item["name"]
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

