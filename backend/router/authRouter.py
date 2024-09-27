from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.responses import JSONResponse
from models.userModel import User
from sqlalchemy.orm import Session
from db.database import get_db
from models.userSchema import userRegister,userLogin
import bcrypt
import re
router=APIRouter()
email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
def valid_email(email):
    return re.match(email_regex,email) is not None


@router.get('/login')
async def userLogin(user:userLogin,db:Session=Depends(get_db)):   
    if not(user.username or user.password):
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content={"message":"both username and password are required"})
        
@router.post('/register')
async def userRegister(user:userRegister,db:Session=Depends(get_db)):
    try:
        if not(user.username or user.password or user.email):
            print("here usename issue")
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content={"message":"All fields are required"})
        elif len(user.username)<6: 
            print("in username")
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content={"message":"username should be ateast 6"})
        elif len(user.password)<6:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content={"message":"passwrod should be atleast 6 character "})
        elif not valid_email(user.emailid):
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content={"message":"please provide an valid email id"})
        existing_user=db.query(User).filter((User.username==user.username)|(User.emailid==user.emailid)).first()
        if existing_user:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content={"message":"user with this credentials already exists"})
        salt=bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), salt).decode('utf-8')
        print(hashed_password)
        new_user=User(username=user.username,password=hashed_password,emailid=user.emailid)
        db.add(new_user)
        db.commit()
        return JSONResponse(status_code=status.HTTP_201_CREATED,content={"message":"User created"})
    except Exception as e:
        return HTTPException(status_code=500,detail=f"internal serveor error {str(e)}")
