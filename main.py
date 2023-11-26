from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from contextlib import asynccontextmanager
import os
import setup_fns

db=0
chatHistory=[]

@asynccontextmanager
async def lifespan(app: FastAPI):
  global db
  db = setup_fns.setup()
  yield
  try:
    os.remove('chatHistory.json')
  except:
    print('chatHistory.json not found')

app = FastAPI(lifespan=lifespan)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
  global chatHistory
  chatHistory = []
  return templates.TemplateResponse("index.html",{"request": request})

@app.get('/getPromptResponse')
def getPromptResponse(request: Request):
  global chatHistory
  query=request.query_params['chatPrompt']
  chatHistory = setup_fns.inputQueryResponse(query, db, chatHistory)
  return templates.TemplateResponse("shortTemplates/chatHistory.html", {"request": request, "chatHistory": chatHistory})