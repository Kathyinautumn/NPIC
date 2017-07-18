import pymysql


class UserPassword():
    def checkPassword(self, username, password):

        conn = pymysql.connect("localhost", "root", "Kathyinautumn6!", "DataAnalysis")
        with conn:
            cursor = conn.cursor()
            args = [str(username)]
            sql = "SELECT * FROM user_password WHERE username IN (%s)"
            in_p = ', '.join(list(map(lambda x: '%s', args)))
            sql = sql % in_p
            cursor.execute(sql, *args)
            data = cursor.fetchall()

            args = [str(password)]
            sql = "SELECT * FROM user_password WHERE password IN (%s)"
            in_b = ', '.join(list(map(lambda x: '%s', args)))
            sql = sql % in_b
            cursor.execute(sql, *args)
            data2 = cursor.fetchall()

            if data == data2:
                return True
            else:
                return False

        cursor.close()
        conn.commit()
        conn.close()
