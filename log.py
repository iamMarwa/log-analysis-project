# !/usr/bin/env python3
import psycopg2
import time


def connect(news):
    try:
        db = psycopg2.connect("dbname={}".format(news))
    except psycopg2.Error as e:
        print("Unable to connect!")
        print(e.pgerror)
        print(e.diag.message_detail)
        sys.exit(1)
    cursor = db.cursor()
    return db, cursor


db, cursor = connect("news")
query1 = "SELECT title, count(path) AS num FROM articles, log \
 WHERE articles.slug = substring(path from 10 for 100) GROUP BY \
 title ORDER BY num DESC LIMIT 3;"
query2 = "SELECT a.name, p.num \
                 FROM authors AS a\
                 INNER JOIN mostAuthor AS p ON p.author = a.id \
                 GROUP BY a.name, p.num \
                 ORDER BY p.num DESC;"
query3 = "SELECT to_char(err.most_day, 'MM/DD/YYYY'),\
 round((err.errors*1.0 / total_re.total*1.0)*100, 2) as per \
  FROM err, total_re WHERE err.most_day = total_re.most_day and \
   (err.errors*1.0 / total_re.total*1.0)*100 > 1 ORDER BY per desc;"


def most_article(query1):
    # db = connect()
    cursor = db.cursor()
    cursor.execute(query1)
    results = cursor.fetchall()
    for i in range(len(results)):
        title = results[i][0]
        views = results[i][1]
        print("%s -- %d views" % (title, views))
    # db.close()


def most_authors(query2):
    # db = connect()
    cursor = db.cursor()
    cursor.execute(query2)
    results = cursor.fetchall()
    for i in range(len(results)):
        name = results[i][0]
        views = results[i][1]
        print("%s -- %d views" % (name, views))
    # db.close()


def error_result(query3):
    # db = connect()
    cursor = db.cursor()
    cursor.execute(query3)
    results = cursor.fetchall()
    for i in range(len(results)):
        date = results[i][0]
        err_prc = results[i][1]
        print("%s -- %.1f %%" % (date, err_prc))


if __name__ == "__main__":
    print("What are the most popular three articles of all time?")
    most_article(query1)
    print("\n")
    print("Who are the most popular article authors of all time?")
    most_authors(query2)
    print("\n")
    print("On which days did more than 1% of requests lead to errors?")
    error_result(query3)
