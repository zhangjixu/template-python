import pandas as pd
from sqlalchemy import create_engine


def read_excel():
    df = pd.read_excel('path', sheet_name='sheet')
    # 只取固定的列
    data = df[['time', 'username', 'tname', 'type', 'ip', 'displayName', 'consume', 'browser']]
    # 时间戳转换为字符串
    data['time'] = pd.to_datetime(data['time'], unit='ms', origin=pd.Timestamp('1970-01-01 08:00:00'))
    # 修改列名
    data.rename(columns={'displayName': 'display_name'}, inplace=True)

    # data['time'] = data['time'].apply(lambda x: time.mktime(time.strptime(x, '%Y-%m-%d %H:%M:%S')))
    # 连接 oracle 数据库
    connect = create_engine('oracle://username:password@host:port/sid')
    data.to_sql('test_dibo', connect, index=False, if_exists='append')


if __name__ == '__main__':
    read_excel()
