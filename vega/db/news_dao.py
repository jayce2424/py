from db.mysql_db import pool

class NewsDao:
    #查询待审批新闻列表
    def search_unreview_list(self,page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select n.id,n.title,t.type,u.username " \
                  "from t_news n join t_type t on n.type_id=t.id " \
                    "join t_user u on n.editor_id=u.id " \
                    "where n.state=%s " \
                    "order by n.create_time desc " \
                    "limit %s,%s"
            #print(sql)
            cursor.execute(sql, ("待审批",(page-1)*10,10))
            result = cursor.fetchall()
            return result

        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    #查询待审批新闻的总页数
    def search_unreview_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select ceil(count(*)/10) from t_news where state=%s"
            cursor.execute(sql, ["待审批"])
            count_page = cursor.fetchone()[0]
            return count_page

        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    #审批新闻
    def update_unreview_news(self,id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "update t_news set state=%s where id=%s"
            cursor.execute(sql, ("已审批",id))
            con.commit()

        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    #查询新闻列表
    def search_list(self,page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select n.id,n.title,t.type,u.username " \
                  "from t_news n join t_type t on n.type_id=t.id " \
                  "join t_user u on n.editor_id=u.id " \
                  "order by n.create_time desc " \
                  "limit %s,%s"
            #print(sql)
            cursor.execute(sql, ((page-1)*10,10))
            result = cursor.fetchall()
            return result

        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    #查询新闻的总页数
    def search_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select ceil(count(*)/10) from t_news "
            cursor.execute(sql)
            count_page = cursor.fetchone()[0]
            return count_page

        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    #删除新闻
    def delete_by_id(self,id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "delete from t_news where id=%s"
            cursor.execute(sql, [id])
            con.commit()

        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    #添加新闻
    def insert(self,title,editor_id,type_id,content_id,is_top):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "insert into t_news(title,editor_id,type_id,content_id,is_top,state) " \
                  "values(%s,%s,%s,%s,%s,%s) "
            cursor.execute(sql, (title,editor_id,type_id,content_id,is_top,"待审批"))
            con.commit()

        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()


    #查找用于缓存的记录
    def search_cache(self,id):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select n.title,u.username,t.type,n.content_id,n.is_top,n.create_time " \
                  "from t_news n " \
                  "join t_type t on n.type_id=t.id " \
                  "join t_user u on n.editor_id=u.id " \
                  "where n.id=%s "
            print(sql)
            cursor.execute(sql, [id])
            result = cursor.fetchone()
            return result

        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

#测试
# service=NewsDao()
# result=service.search_cache(1)
# print(result)