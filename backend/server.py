from fastapi import FastAPI
from router.authRouter import router as authRouter
from db.database import Base,engine
app=FastAPI()


app.include_router(authRouter,prefix='/auth',tags=['users'])
@app.get('/',tags=['ping'])
async def ping():
    return {"message":"ping working"}
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)