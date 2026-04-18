from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Vivek Azure Web App"

@app.route("/env")
def get_env():
    value = os.getenv("MY_MESSAGE", "No env variable found")
    return f"ENV VALUE: {value}"