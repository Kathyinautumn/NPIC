import pymysql

db = pymysql.connect("localhost", "root", "Kathyinautumn6!", "DataAnalysis")

cursor = db.cursor()

# sql = "INSERT INTO trade (time_start, time_end, file_path) VALUES (%s, %s, '%s')"
# data= (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") )

sql = "SELECT * FROM file_path"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for column in results:
        id = column[0]
        time_start = column[1]
        time_end = column[2]
        file_path = column[3]
        print("id=%s,time_start=%s,time_end=%s,file_path=%s" % \
          (id, time_start, time_end, file_path))
except Exception as e:
    print(Exception, ":", e)

finally:
    db.close()
