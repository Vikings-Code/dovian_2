from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://0f0rsrgt43oubj034u30:pscale_pw_5PmhLyRtXH7X3xoxbiPFcSEK52O5Suv8rZ4xXUrM0ZH@aws.connect.psdb.cloud/dovian?charset=utf8mb4"

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
