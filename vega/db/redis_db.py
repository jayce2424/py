import redis

try:
    pool = redis.ConnectionPool(
        host="10.10.18.87",
        port=6379,
        password="123456",
        db=1,
        max_connections=20
    )
except Exception as e:
    print(e)

#redis缓存的是新闻的明确内容，而不是id