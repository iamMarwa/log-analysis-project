import psycopg2

db = psycopg2.connect("dbname=news")
c = db.cursor()
print("What are the most popular three articles of all time?")
c.execute("SELECT title, count(path) AS num FROM articles, \
                 log WHERE articles.slug = substring(path from 10 for 100)\
                 GROUP BY title ORDER BY num DESC LIMIT 3;")
result = c.fetchall()
print (result)


print("Who are the most popular article authors of all time?")
c.execute("SELECT a.name, p.num \
                 FROM authors AS a\
                 INNER JOIN mostAuthor AS p ON p.author = a.id \
                 GROUP BY a.name, p.num \
                 ORDER BY p.num DESC;")
result = c.fetchall()
print (result)
print("On which days did more than 1% of requests lead to errors?")
c.execute("select to_char(time, 'Mon DD, YYYY'), 100. * count(*) / sum(count(*)) over () as num from log where status NOT LIKE '%200 OK%' group by time order by num desc limit 1;")
posts = c.fetchall()
db.close()
print (posts)