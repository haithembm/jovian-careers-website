from flask import Flask
app = Flask(__name__)

@app.route("/")

def Hello_world():
    return "Hello!"

if __name__ == "__main__":  
    # on running python app.py    
    app.run( host='0.0.0.0',debug=True)         # run the flask app"