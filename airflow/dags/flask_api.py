from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    data = {
        'name':'Abhijit',
        'age': '23',

    }
    return(data)
