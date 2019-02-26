import psycopg2
import os

def get():
    con = psycopg2.connect(host='db', database='reviewdb', user=os.environ['POSTGRES_USER'], password=os.environ['POSTGRES_PASSWORD'])
    cur = con.cursor()
    cur.execute("select * from reviewsites where (last_crawl is null or reviewsites.last_crawl >  NOW() - '14 days'::INTERVAL)")
    return cur.fetchall()

