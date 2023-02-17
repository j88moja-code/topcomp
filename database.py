from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://vme1vzyrevb959y4tx94:pscale_pw_4FgQccqO6Bl0oqCRVu4MGe8LyqemQzA2zkxpQzyxSSt@us-east.connect.psdb.cloud/topcomp?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem",
                       }})

with engine.connect() as conn:
  result = conn.execute(text("select * from laptop"))
  result_dicts = []
  for row in result.all():
    result_dicts.append(dict(row))
  print(result_dicts)
