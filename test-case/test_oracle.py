from module.OpsOracle import OpsOracle


def query_oracle_util():
    oracle = OpsOracle()
    sql = 'select * from test.test'
    rs = oracle.query(sql)
    print(rs)


def update_oracle_util():
    oracle = OpsOracle()
    sql = '''delete from test.test where 1 = :id '''
    json = {'id': 1}
    oracle.update(sql, json)


def insert_many_oracle_util():
    oracle = OpsOracle()
    sql = ''' insert into test.TEST(id, NAME, AGE) values(:id, :name, :age) '''
    datas = list()
    datas.append({'id': 3, 'name': '王五', 'age': 21})
    datas.append({'id': 4, 'name': '赵六', 'age': 22})
    oracle.insert_many(sql, datas)


def insert_one_oracle_util():
    oracle = OpsOracle()
    sql = ''' insert into test.TEST(id, NAME, AGE) values(:id, :name, :age) '''
    data = {'id': 3, 'name': '王五', 'age': 20}
    oracle.update(sql, data)


if __name__ == '__main__':
    query_oracle_util()
