import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='bob', passwd='123456', db='xhamster')

try:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM tests")

    print(cur.description)

    for row in cur:
        print(row)
finally:
    conn.close()