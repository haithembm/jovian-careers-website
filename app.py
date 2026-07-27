from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db


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
    jobs  = load_jobs_from_db()
    return render_template("home.html", 
                           jobs=jobs
                            )


@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not Found", 404
    return render_template("jobpage.html", job=job)



@app.route("/api/jobs")
def list_jobs():
    jobs  = load_jobs_from_db()
    return jsonify(jobs)


if __name__ == "__main__":  
    # on running python app.py    
    app.run( host='0.0.0.0',debug=True,port=5001)         # run the flask app"