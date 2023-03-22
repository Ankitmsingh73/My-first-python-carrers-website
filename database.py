from sqlalchemy import create_engine,text


db_connection_string="mysql+pymysql://cqdgsa810jsi46eqskeq:pscale_pw_iW0BmPRy2XIQ9PFdDXRFmIBgHp6eiiuxIPxW2cKRxKL@ap-south.connect.psdb.cloud/myapp?charset=utf8mb4"
engine = create_engine(db_connection_string,connect_args={
  "ssl":{
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})


# with engine.connect() as con:
#   result = con.execute(text("select * from jobs"))
#   print("type of result:-",type(result))
#   result_all = result.all()
#   print("type of result_all",type(result_all))
#   print(result_all)
#   print("--------dict--")
#   for row in result_all:
#     row_as_dict = row._mapping
#   print(row_as_dict)

def load_jobs_from_db():
  with engine.connect() as con:
    result = con.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._mapping)
    return jobs