# !/usr/bin/env python

import psycopg2
import time

DBNAME = "news"

questionOne = "What are the most popular three articles of all time?"

queryOne = ("SELECT title, COUNT(title) AS num FROM \
articles INNER JOIN log ON log.path LIKE CONCAT('/article/', articles.slug) \
GROUP BY log.path, articles.title ORDER BY num DESC LIMIT 3;")

questionTwo = "Who are the most popular article authors of all time?"

queryTwo = ("SELECT authors.name, COUNT(*) AS num\
 FROM articles INNER JOIN authors \
ON articles.author = authors.id \
INNER JOIN log \
ON log.path = CONCAT('/article/', articles.slug)\
GROUP BY authors.name\
 ORDER BY num DESC\
 LIMIT 4;")

questionThree = "On which days did more than 1% of requests lead to errors?"

queryThree = ("SELECT to_char(err.most_day, 'MM/DD/YYYY'),\
 round((err.errors*1.0 / total_re.total*1.0)*100, 2) as per \
  FROM err, total_re WHERE err.most_day = total_re.most_day and \
   (err.errors*1.0 / total_re.total*1.0)*100 > 1 ORDER BY per desc;")


def results(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


question1 = results(queryOne)
question2 = results(queryTwo)
question3 = results(queryThree)


def printTheResult(result):
    for i in range(len(result)):
        title = result[i][0]
        views = result[i][1]
        print("\t" + "%s - %d" % (title, views) + " views")
    print("\n")


def printquestion3(resultt):
    for i in range(len(resultt)):
        date = resultt[i][0]
        prc = resultt[i][1]
        print("%s -- %.1f %%" % (date, prc))


print(questionOne)
printTheResult(question1)
print(questionTwo)
printTheResult(question2)
print(questionThree)
printquestion3(question3)
