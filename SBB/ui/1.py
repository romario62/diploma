# -*- coding: utf-8 -*-
__author__ = 'roman'

from psycopg2 import sql
import psycopg2
import hashlib

def hashpass(w): #принимает на вход пароль и шифрует в мд5
    password = str(w)
    bpass = bytes(password, 'utf8')
    hash_object = hashlib.md5(bpass)
    md = hash_object.hexdigest()
    return md

login = str(input())
password = str(input())
hpass = hashpass(password)
print(hpass)
conn = psycopg2.connect(dbname='ticket', user='postgres', password='1234', host='localhost', port='5432')
with conn.cursor() as cursor:
    conn.autocommit = True
    cursor.execute("select * from users")
    row = cursor.fetchall()
    for l in row:
        print(l[0])
        print(l[1])
        print(l[2], "\n")
    if not login in l and hpass in l :
        print('err')
    else:
        print('suck') #это работает, надо только с принт чтото сделать