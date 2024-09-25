from fastapi import APIRouter,Depends
from models import userModel
from sqlalchemy.orm import Session
from db.database import get_db
router=APIRouter()

@router.get('/login')
async def userLogin(db:Session=Depends(get_db)):   
    user=userModel.User(username="sanosh")
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message":"user login"}
