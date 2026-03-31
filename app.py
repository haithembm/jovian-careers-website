from flask import Flask, render_template, jsonify

app = Flask(__name__)

Jobs = [
    {'id' : 1,
        'title' :'Data Analyst',
         'location' : 'Bengaluru, India',
         'salary' : 'Rs. 1000000',
           },
    {'id' : 2,
        'title' :'Data Scientist',
         'location' : 'Delhi, India'
           },
    {'id' : 3,
        'title' :'Frontend Engineer',
         'location' : 'Remote',
         'salary' : 'Rs. 1300000',
           },
    {'id' : 4,
        'title' :'Backtend Engineer',
         'location' : 'San Fran',
         'salary' : '$ 130',
           }

]

@app.route("/")
def Hello_world():
    return render_template("home.html", 
                           jobs=Jobs,
                           company_name=   "Jovian" )


@app.route("/api/jobs")
def list_jobs():
    return jsonify(Jobs)


if __name__ == "__main__":  
    # on running python app.py    
    app.run( host='0.0.0.0',debug=True,port=5001)         # run the flask app"