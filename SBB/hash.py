import psycopg2
with closing(psycopg2.connect(dbname='t', user='postgres', password='1234', host='localhost', port='5432')) as conn:
    with conn.cursor() as cursor:
        conn.autocommit = True
        cursor.execute('select login from users')
        users = cursor.fetchall()
        for row in users:
            print(row)