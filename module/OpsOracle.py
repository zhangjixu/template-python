from module.OracleUtils import OracleUtils
from conf import oracle_config as cfg


class OpsOracle(object):

    def query(self, sql, value={}):
        """
        查询方法
        Args:
            sql:
            value:

        Returns:

        """
        with OracleUtils(host=cfg.ORACLE_HOST, port=cfg.ORACLE_PORT, database=cfg.ORACLE_DATABASE,
                         user=cfg.ORACLE_USERNAME, password=cfg.ORACLE_PASSWORD) as cnx:
            cur = cnx.cursor()
            cur.execute(sql, value)
            return cur.fetchall()

    def update(self, sql, value={}):
        """
        单条记录保存 更新 删除操作
        Args:
            sql:
            value:

        Returns:

        """
        with OracleUtils(host=cfg.ORACLE_HOST, port=cfg.ORACLE_PORT, database=cfg.ORACLE_DATABASE,
                         user=cfg.ORACLE_USERNAME, password=cfg.ORACLE_PASSWORD) as cnx:
            cur = cnx.cursor()
            cur.execute(sql, value)
            cnx.commit()

    def insert_many(self, sql, datas=list()):
        """
        批量插入
        Args:
            sql:
            datas:

        Returns:

        """
        with OracleUtils(host=cfg.ORACLE_HOST, port=cfg.ORACLE_PORT, database=cfg.ORACLE_DATABASE,
                         user=cfg.ORACLE_USERNAME, password=cfg.ORACLE_PASSWORD) as cnx:
            cur = cnx.cursor()
            cur.executemany(sql, datas)
            cnx.commit()
