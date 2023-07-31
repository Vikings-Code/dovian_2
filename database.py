from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://vsiz0lyhcck34qfhtoh6:pscale_pw_VXacN3LmaldE6V9JfcLtVfx0850XExWnXakLTPZN8tb@aws.connect.psdb.cloud/dovian?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
    pool_pre_ping=True,
    connect_args={
        "ssl": {
            "ca": "/etc/ssl/cert.pem"
        }
    })

with engine.connect() as connection:
    result = connection.execute(text("select * from jobs"))

    result_dicts = []
    for row in result.all():
        result_dicts.append(dict(row))

    print(result_dicts)
