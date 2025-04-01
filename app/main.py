from fastapi import FastAPI
from app.presentation.routes.quote import router as quote
app = FastAPI()

app.include_router(quote)
