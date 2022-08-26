from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import page
from routes import api
##############################################

app = FastAPI()

# Static Files 
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include Routes 
app.include_router(page.router)
app.include_router(api.router)