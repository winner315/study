import os

import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password=os.environ.get("DB_PASSWORD", "root"),
    database='interview',
    charset="utf8mb4",
)


def query(sql, params=None):
    """查询：只读，返回所有行（元组的元组）。"""
    cur = conn.cursor()
    try:
        cur.execute(sql, params)
        return cur.fetchall()
    finally:
        cur.close()


def execute(sql, params=None):
    """写操作：提交事务，返回受影响行数；出错回滚并抛出。"""
    cur = conn.cursor()
    try:
        n = cur.execute(sql, params)
        conn.commit()
        return n
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
