
# Logs-analysis
This project is part of the Full Stack Web Developer nanodegree from udacity.

## Prerequirements
* [Python3](https://www.python.org/downloads/)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)

## How To Run The Program:
1. Download or clone repository on you machine.
2. Bring the project directory under the vagrant directory.
3. Start the virtual machine using vagrant up
command.
4. After that, run vagrant ssh log in to your VM.
5. Download the database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
6. To load the data, cd into the vagrant directory and use the command:
```
psql -d news -f newsdata.sql
```
Use this command in order to access the database:
```
psql news
```
7. Go to log-analysis-project directory with
cd /vagrant/log-analysis-project
8. Run log.py file to analyse the log data from the database using
```
python3 log.py
```
9. Go to output.txt file to discover what kind of article's the site's readers like.
10. Shutdown the VM with CTRL + D

 ## SQL View:

The following SQL view are required to run the program. Run psql news inside the /vagrant directory and either copy paste them individually or type them manually.
```
CREATE VIEW mostAuthor AS SELECT author, count(log.path) AS num FROM articles, log WHERE articles.slug = substring(path from 10 for 100) GROUP BY author ORDER BY num DESC LIMIT 4;
```

This statements mean that "Create view to find relationships between authors and relevant logs"

```
CREATE VIEW requests AS
SELECT count(*) AS total,
       date(TIME) AS date
FROM log
GROUP BY date
ORDER BY total DESC;
```
This statements mean that "Create view to find the most day has requests"

```
CREATE VIEW errors AS
SELECT count(*) AS COUNT,
       date(TIME) AS date
FROM log
WHERE status!='200 OK'
GROUP BY date
ORDER BY COUNT DESC;
```
This statements mean that "Create view to find the requests that wasn't '200 OK' "

```
CREATE VIEW percent AS
SELECT requests.date,
       round((100.0*errors.count)/requests.total,2) AS percent
FROM errors,
     requests
WHERE errors.date=requests.date;
```
This statements mean that "Create view to see the errors percent"
