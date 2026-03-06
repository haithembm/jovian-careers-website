from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def Hello_world():
    return render_template("home.html")

if __name__ == "__main__":  
    # on running python app.py    
    app.run( host='0.0.0.0',debug=True,port=5001)         # run the flask app"