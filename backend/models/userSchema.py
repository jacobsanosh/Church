from pydantic import BaseModel
class userRegister(BaseModel):
    username:str
    emailid:str
    password:str
class userLogin(BaseModel):
    username:str 
    password:str 