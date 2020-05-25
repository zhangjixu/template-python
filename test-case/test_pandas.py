import pandas as pd
import time
from sqlalchemy import create_engine


def read_excel():
    df = pd.read_excel('D:\\log.xlsx', sheet_name='sheet')
    # 只取固定的列
    data = df[['time', 'username', 'tname', 'type', 'ip', 'displayName', 'consume', 'browser']]
    # 时间戳转换为字符串
    # data['time'] = pd.to_datetime(data['time'], unit='ms', origin=pd.Timestamp('1970-01-01 08:00:00'))
    # 使用自定义函数进行转换
    data['time'] = data['time'].apply(ts_str)
    # 修改列名
    data.rename(columns={'displayName': 'display_name'}, inplace=True)
    print(data['time'])

    # data['time'] = data['time'].apply(lambda x: time.mktime(time.strptime(x, '%Y-%m-%d %H:%M:%S')))
    # 连接 oracle 数据库
    # connect = create_engine('oracle://username:password@host:port/sid')
    # data.to_sql('test_dibo', connect, index=False, if_exists='append')


def ts_str(ts):
    '''
    时间戳转字符串
    Args:
        ts: 13 位时间戳

    Returns: 返回格式化的字符串时间

    '''
    try:
        st = time.localtime(ts / 1000)
        return time.strftime('%Y-%m-%d %H:%M:%S', st)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    read_excel()
