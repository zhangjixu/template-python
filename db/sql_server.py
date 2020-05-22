import pymssql
from conf import sql_server_config as cfg


def query():
    connect = pymssql.connect(host=cfg.MS_HOST, user=cfg.MS_USER, password=cfg.MS_PASSWORD, database=cfg.MS_DATABASE,
                              charset='utf8')
    cursor = connect.cursor()
    sql = "select convert(varchar(10),GETDATE(),120)"
    cursor.execute(sql)
    rs = cursor.fetchall()
    for data in rs:
        print(data)

    cursor.close()
    connect.close()


def update():
    connect = pymssql.connect(host=cfg.MS_HOST, user=cfg.MS_USER, password=cfg.MS_PASSWORD, database=cfg.MS_DATABASE,
                              charset='utf8')
    cursor = connect.cursor()
    sql = "update test set name = 'lisi' where ia = 1"
    cursor.execute(sql)
    connect.commit()
    cursor.close()
    connect.close()


if __name__ == '__main__':
    query()
