import psycopg2
import os


con = psycopg2.connect(host='db', database='reviewdb', user=os.environ['POSTGRES_USER'], password=os.environ['POSTGRES_PASSWORD'])

def get():

    try:
        cur = con.cursor()
        cur.execute("select * from reviewsites where (last_crawl is null or reviewsites.last_crawl >  now() - '14 days'::INTERVAL)")
        results = cur.fetchall()
        cur.close()
    except Exception as e:
        print(e)
    return results

def setParsed(url):
    update_sql = "update reviewsites set last_crawl = now() where url = %s"

    try:
        cur = con.cursor()
        cur.execute(update_sql, (url,))
        con.commit()
        cur.close()
    except Exception as e:
        print(e)