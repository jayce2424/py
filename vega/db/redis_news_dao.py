from db.redis_db import pool
import redis

class RedisNewsDao:
    #
    def insert(self,id,title,username,type,content,is_top,create_time):
        con=redis.Redis(
            connection_pool=pool
        )
        try:
            con.hmset(id,{
                "title":title,
                "author":username,
                "type":type,
                "content":content,
                "is_top":is_top,
                "create_time":create_time
            })
            # is_top>0没有过期时间；=0是24小时，不置顶
            if is_top==0:
                con.expire(id,24*60*40)

        except Exception as e:
            print(e)
        finally:
            del con
