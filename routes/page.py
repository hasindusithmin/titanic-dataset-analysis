
from fastapi import APIRouter,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
    tags=['Pages']
)

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def get_home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/gender", response_class=HTMLResponse)
def get_gender_page(request: Request):
    return templates.TemplateResponse("gender.html", {"request": request})

