import cx_Oracle
from DBUtils.PooledDB import PooledDB


class OracleUtils(object):

    def __init__(self, host, port, database, user, password):
        """
        建立连接
        :param host:
        :param port:
        :param database:
        :param user:
        :param password:
        """
        dsn = host + ':' + str(port) + '/' + database
        self._dsn = dsn
        self._user = user
        self._password = password
        # mincached ：启动时开启的空连接数量 blocking ：达到最大数量时是否阻塞
        self.pool = PooledDB(creator=cx_Oracle, mincached=20, blocking=True, user=user, password=password, dsn=dsn)

    def __enter__(self):
        self.conn = self.pool.connection()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
