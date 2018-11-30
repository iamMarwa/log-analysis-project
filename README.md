{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf600
{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;\f1\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red27\green31\blue34;\red10\green77\blue204;\red255\green255\blue255;
\red21\green23\blue26;\red53\green53\blue53;}
{\*\expandedcolortbl;;\cssrgb\c14118\c16078\c18039;\cssrgb\c1176\c40000\c83922;\cssrgb\c100000\c100000\c100000;
\cssrgb\c10588\c12157\c13725\c4706;\cssrgb\c27059\c27059\c27059;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{decimal\}.}{\leveltext\leveltemplateid1\'02\'00.;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listname ;}\listid1}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}}
\paperw11900\paperh16840\margl1440\margr1440\vieww13260\viewh10200\viewkind0
\deftab720
\pard\pardeftab720\sl600\sa320\partightenfactor0

\f0\b\fs48 \cf2 \expnd0\expndtw0\kerning0
# Logs-analysis\
\pard\pardeftab720\sl360\sa320\partightenfactor0

\b0\fs32 \cf2 This project is part of the Full Stack Web Developer nanodegree from udacity.\
\pard\pardeftab720\sl360\partightenfactor0

\b\fs36 \cf3 \
\pard\pardeftab720\sl440\sa320\partightenfactor0
\cf2 ## Prerequirements\
* [Python3](https://www.python.org/downloads/)\
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)\
* [Vagrant](https://www.vagrantup.com/downloads.html)
\b0\fs32 \
\pard\tx566\pardeftab720\sl360\partightenfactor0
\cf2 \
\pard\pardeftab720\sl600\sa320\partightenfactor0

\b\fs48 \cf2 ## How To Run The Program:
\fs32 \cf3 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\sl360\partightenfactor0
\ls1\ilvl0
\b0 \cf2 \cb4 \kerning1\expnd0\expndtw0 {\listtext	1.	}\expnd0\expndtw0\kerning0
Download or clone repository on you machine.\cb1 \
\ls1\ilvl0\cb4 \kerning1\expnd0\expndtw0 {\listtext	2.	}\expnd0\expndtw0\kerning0
Bring the project directory under the vagrant directory.\cb1 \
\ls1\ilvl0\cb4 \kerning1\expnd0\expndtw0 {\listtext	3.	}\expnd0\expndtw0\kerning0
Start the virtual machine using\'a0
\f1\fs27\fsmilli13600 \cb5 vagrant up
\f0\fs32 \cb4 \'a0command.\cb1 \
\ls1\ilvl0\cb4 \kerning1\expnd0\expndtw0 {\listtext	4.	}\expnd0\expndtw0\kerning0
After that, run\'a0
\f1\fs27\fsmilli13600 \cb5 vagrant ssh
\f0\fs32 \cb4 \'a0to log in to your VM.\cb1 \
\ls1\ilvl0\cb4 \kerning1\expnd0\expndtw0 {\listtext	5.	}\expnd0\expndtw0\kerning0
Go to log-analysis-project directory with\'a0
\f1\fs27\fsmilli13600 \cb5 cd /vagrant/log-analysis-project
\f0\fs32 \cb4 .\cb1 \
\ls1\ilvl0\cb4 \kerning1\expnd0\expndtw0 {\listtext	6.	}\expnd0\expndtw0\kerning0
Run log.py file to analyse the log data from the database using\'a0
\f1\fs27\fsmilli13600 \cb5 python3 log.py
\f0\fs32 \cb4 .\cb1 \
\ls1\ilvl0\cb4 \kerning1\expnd0\expndtw0 {\listtext	7.	}\expnd0\expndtw0\kerning0
Go to output.txt file to discover what kind of article's the site's readers like.\cb1 \
\ls1\ilvl0\cb4 \kerning1\expnd0\expndtw0 {\listtext	8.	}\expnd0\expndtw0\kerning0
Shutdown the VM with\'a0
\f1\fs27\fsmilli13600 \cb5 CTRL + D
\f0\fs32 \cb4 .\
\pard\tx566\pardeftab720\sl360\partightenfactor0
\cf2 \cb1 \
\pard\pardeftab720\sl600\sa320\partightenfactor0

\b\fs48 \cf2 ## SQL View:\
\pard\pardeftab720\sl360\partightenfactor0

\b0\fs32 \cf2 \cb4 The following SQL view are required to run the program. Run\'a0
\f1\fs27\fsmilli13600 \cb5 psql news
\f0\fs32 \cb4 \'a0inside the /vagrant directory and either copy paste them individually or type them manually.
\b\fs48 \cb1 \
\pard\tx566\pardeftab720\sl360\partightenfactor0

\b0\fs32 \cf2 \
\pard\pardeftab560\slleading20\partightenfactor0

\fs24 \cf6 \kerning1\expnd0\expndtw0 CREATE VIEW mostAuthor AS SELECT author, count(log.path) AS num FROM articles, log WHERE articles.slug = substring(path from 10 for 100) GROUP BY author ORDER BY num DESC LIMIT 4;\
\pard\pardeftab720\sl360\partightenfactor0

\fs32 \cf2 \cb4 \expnd0\expndtw0\kerning0
This statements mean that "Create view to find relationships between authors and relevant logs".\cb1 \
\pard\tx566\pardeftab720\sl360\partightenfactor0
\cf2 \
\
}