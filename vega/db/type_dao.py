from db.mysql_db import pool

class TypeDao:
    #查询新闻列表
    def search_list(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select id,type from t_type order by id"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()