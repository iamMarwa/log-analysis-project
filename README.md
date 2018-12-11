
# Logs-analysis
This project is for the Full Stack Web Developer nanodegree from udacity.

## Prerequirements
* [Python3](https://www.python.org/downloads/)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)

## How To Run The Program:
1. Download or clone the project on your machine under the vagrant directory by using:
```
git clone https://github.com/iamMarwa/log-analysis-project.git
```
2. Start the virtual machine by using this command under the vagrant directory:
```
vagrant up
```
3. Then to log in to your virtual machine you'll need to use this command:
```
vagrant ssh
```
4. Download the database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
5. To load the data, cd into the vagrant directory and use the command:
```
psql -d news -f newsdata.sql
```
Use this command in order to access the database:
```
psql news
```
6. Go to the project directory by using:
```
cd log-analysis-project
```
7. To run the project and see the output run:
```
python3 log.py
```

 ## SQL View:

The following SQL view are required to run the program. Run psql news inside the /vagrant directory and either copy paste them individually or type them manually.

```
CREATE VIEW total_re AS SELECT DATE(time) AS most_day, COUNT(status) AS total FROM log GROUP BY most_day ORDER BY most_day;
```
This statements mean that "Create view to find the most day has requests"

```
CREATE VIEW err AS SELECT date(TIME) AS most_day, count(*) AS errors FROM log WHERE NOT status='200 OK' GROUP BY most_day ORDER BY most_day;
```
This statements mean that "Create view to find the requests that wasn't '200 OK' "

```
