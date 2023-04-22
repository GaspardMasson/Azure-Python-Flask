from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"




#https://stravaappwebhook.azurewebsites.net/webhook