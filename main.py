import pandas as pd
import multiprocessing
import psycopg2
print ("Connecting Postgresql..")
def pg_sql ():
    
    conn_psql =  psycopg2.connect(
    host="pg-server",
    database="mydb",
    user="myuser",
    password="mypass")

    cur = conn_psql.cursor()
    #dml = """create table myschema.mytab (id int)"""
    insert = """insert into myschema.mytab values (100)"""
    cur.execute (insert)
    conn_psql.commit()
    conn_psql.close()
    return "Inserted"
result = pg_sql()
print (result)