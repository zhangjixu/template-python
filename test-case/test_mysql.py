from module.OpsMysql import OpsMysql


def query():
    ops = OpsMysql()
    sql = "select * from `tmp`"
    data = ops.query(sql)
    for row in data:
        print(row)


if __name__ == '__main__':
    query()
