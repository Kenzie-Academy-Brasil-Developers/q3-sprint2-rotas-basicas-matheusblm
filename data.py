# Código do dev aqui
from flask import Flask
from datetime import datetime


app = Flask(__name__)


@app.get("/")

def home():
    return {"data": "Hello Flask"}

@app.get("/current_datetime")

def currentime():
    now = datetime.now()
    if int(now.strftime("%H")) > 12 and int(now.strftime("%H")) < 18:
        greet = "Boa tarde!"
    elif int(now.strftime("%H")) < 12:
        greet = "Bom dia!" 
    else:
        greet = "Boa noite!"
    date = now.strftime("%C/%m/%Y %H:%M:%S")
    return {"current_datetime": f"{date}", "message":  greet }
