import sqlalchemy
from sqlalchemy import create_engine, text
import urllib.parse
import pymysql
import os


raw_password = "p@ss:w/ord"
safe_password = urllib.parse.quote_plus(raw_password)

# Safely inject into your connection string
url = f"{os.environ['DB_CONNECTION_STRING']}"

engine = create_engine(url)


with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    
    results_dicts =  [ (row._asdict())  for row in result.all()  ]
     



def load_jobs_from_db():

    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))

        jobs =  [ (row._asdict())  for row in result.all()  ]
        return jobs



def load_job_from_db(id):
     with engine.connect() as conn:
          result = conn.execute(
               text("SELECT * FROM jobs WHERE id = :val"),
               {"val": id}
          )
          rows = result.all()
          if len(rows) == 0:    
               return None
          else:
              return rows[0]._asdict()



