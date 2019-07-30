# 创建连接池
import mysql.connector.pooling

__config = {
    "host": "192.168.10.200",
    "port": 3306,
    "user": "app",
    "password": "app123",
    "database": "vega"
}
try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **__config,
        pool_size=10
    )
    con = pool.get_connection()
    con.start_transaction()

except Exception as e:
    print(e)
