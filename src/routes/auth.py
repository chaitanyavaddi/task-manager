from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from src.config.db import db

templates = Jinja2Templates(directory="templates")


router = APIRouter()

@router.get('/login')
def show_signup_page(request: Request):
    # if request.cookies.get('user_session'):
    #     return templates.TemplateResponse("dashboard.html", {'request': request}) 
    return templates.TemplateResponse("login.html", {"request": request})


@router.post('/login')
def signup_user(request: Request, email = Form(...), password = Form(...)):
    result = db.auth.sign_in_with_password({
        "email": email,
        "password": password
    })

    if result.session.access_token:
        response = RedirectResponse('/dashboard')

        response.set_cookie(key="user_session", value=result.session.access_token, max_age=3600)

        return response