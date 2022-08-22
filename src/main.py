from fastapi import FastAPI, Request, Response, Depends, staticfiles
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


# Pages
@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Friends Connect - Home"})


@app.get("/login", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "title": "Friends Connect - Login"})


# API
@app.post("/login", response_class=RedirectResponse)
def login(request: Request, response: Response,
          form_data: OAuth2PasswordRequestForm = Depends()):


