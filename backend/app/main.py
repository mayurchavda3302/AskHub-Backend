from fastapi import FastAPI
from database import engine, Base
from auth import models as auth_models
from qa import models as qa_models
from auth.routes import router as auth_router
from qa.routes import router as qa_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(qa_router, prefix="/qa", tags=["qa"])
