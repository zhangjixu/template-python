import pymongo
import time
import bson
from module.MongoUtils import MongoUtils
from bson.objectid import ObjectId


def query():
    """
    用于简单查询 mongo 数据
    Returns:

    """
    collection = MongoUtils(u'test', u'user').get_mongo_collection()
    cursor = collection.find()
    for doc in cursor:
        print(doc)

    cursor.close()


def query_sort():
    '''
    mongo 查询
    排序
    limit 操作
    noCursorTimeout 设置为 true
    Returns:

    '''
    collection = MongoUtils(u'acrm', u'policy_result').get_mongo_collection()
    document = {u'ut': {u'$gte': 1504022400000, u'$lt': 1504540800000}}
    # 按照 pymongo.ASCENDING 表示升序排序
    # pymongo.DESCENDING 表示降序
    cursor_ = collection.find(document, no_cursor_timeout=True).sort([(u'ut', pymongo.ASCENDING)]).limit(5)
    for docu in cursor_:
        ut = docu[u'ut']
        date_str = ts_str(ut / 1000)
        print(date_str)


def ts_str(ts):
    '''
    10 位数字转字符串
    Args:
        ts: 十位数字

    Returns:

    '''
    st = time.localtime(ts)
    return time.strftime('%Y-%m-%d %H:%M:%S', st)


def query_oplog():
    '''
    用于查询 oplog 日志
    Returns:

    '''
    collection = MongoUtils(u'local', u'oplog.rs').get_mongo_collection()
    oplog_start = bson.timestamp.Timestamp(1533528000, 0)
    oplog_end = bson.timestamp.Timestamp(1536207400, 0)
    document = {u'ts': {u'$gte': oplog_start, u'$lt': oplog_end}}
    cursor_ = collection.find(document, cursor_type=pymongo.CursorType.TAILABLE_AWAIT, oplog_replay=True).limit(10)
    for docu in cursor_:
        print(docu['ts'])
        print(docu['op'])


def save():
    '''
    用于保存 mongo 数据
    Returns:

    '''
    collection = MongoUtils(u'test', u'user').get_mongo_collection()
    document = {u'name': u'李四', u'age': 20}
    collection.insert_one(document)
    print(u'success')


if __name__ == '__main__':
    query()
