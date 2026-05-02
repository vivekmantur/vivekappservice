from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Vivek Azure Web App"

@app.route("/env")
def get_env():
    value = os.getenv("MY_MESSAGE", "No env variable found")
    return f"ENV VALUE: {value}"

if __name__ == "__main__":
    app.run(debug=True)