# Logs Analysis
You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
## Prerequisites
* To start on this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze,We're using tools called `Vagrant` and `VirtualBox` to install and manage the VM.
* You'll be doing these exercises using a Unix-style terminal on your computer. If you are using a **Mac**  or **Linux** system, your regular terminal program will do just fine. On **Windows**, we recommend using the **Git Bash** terminal that comes with the Git software.
* Download the **VM** configuration.
## Installing
* a. Vagrant: https://www.vagrantup.com/downloads.html
* Virtual Machine: https://www.virtualbox.org/wiki/Downloads
* Download a FSND virtual machine:https://github.com/udacity/fullstack-nanodegree-vm
   and probably you will find the file in your “Download” folder.
* we recommend using the **Git Bash** terminal that comes with the Git
  software. If you don't already have Git installed, download Git from git-scm.com.
### Examples
#### Command Line
`vagrant --version`
- If Vagrant is successfully installed, you will be able to run vagrant --version
in your terminal to see the version number.
## Running the tests
* Once you get the above software installed, follow the following instructions:
`cd vagrant`
`vagrant up`
`vagrant ssh`
`cd /vagrant`
`mkdir log-analysis-project`
`cd log-analysis-project`
- For this project, all the work will be on your Linux machine, so always make sure
you logged in by using the following commands: vagrant up, then vagrant ssh, 
then cd /vagrant.
Note: Files in the VM's /vagrant directory are shared with the vagrant folder on     your computer. But other data inside the VM is not.
## Download and Load the Data
* For this project, you need to download “newsdata.sql” from the project page or by clicking on the following link: https://github.com/udacity/fullstack-nanodegree-vm
*  Move the “newsdata.sql” to your project folder “log-analysis-project”
*  Load the data from the “newsdata.sql” by using the following command: Note that we are using PostgreSQL for this project:
`psql -d news -f newsdata.sql`
* Once you have the data loaded into your database, connect to your database using:
`psql -d news`
## Explore the Data
`\dt`: display tables — lists the tables that are available in the database
`\d` table_name: shows the database schema for that particular table
* The “newsdata.sql” has three different tables:
i. Authors: table includes information about the authors of articles.
ii. Articles: table includes the articles themselves.
iii. Log: table includes one entry for each time a user has accessed the site.
## Create a Python File and Output Text File
* The main purpose of this project is building a python code using “psycopg2” module that
answers the following three questions by using “newsdata.sql”:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?
I. In your python code you need to import psycopg2 library and you need to install the package from the terminal/git bash if you have not yet:
`pip3 install psycopg2`
II. Create a three SQL statement that answers the above questions.
III. Create a function to connect your code and database, fetch data and execute the SQL statements.
IV. Print out the results and make sure you follow the project print out formats.
For example:
a. Question1: “Article Name” – numberOfView views
b. Question 2: author’s Name – numberOfView views
c. Question 3: Mon DD, YYYY – percentage% errors
d. Exactly as it is shown in project page.
V. Test your code by running your python file from git bash/ terminal
`python news.py`
## Coding Style
* SQL Query: Make sure each question is answered by one single query. Capitalize the
keywords such as WHERE FROM AS …… etc.
*  Python code: Use a style standard to test your python code quality like “pycodestyle”.Your code should pass the style standard with 0 errors.
`pip3 install pycodestyle`
### Examples
#### API
  ```
#!/usr/bin/env python3
from datetime import datetime
import psycopg2


def log_anlys():
    """Return the most popular three articles of all time."""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("""select path, count(*) as views from log, articles
                 where log.path = '/article/' || articles.slug group by 1
                 order by 2 desc limit 3 """)
    sul_1 = c.fetchall()
    for key, v in sul_1:
        key = key.split('/')[2]
        key = key.replace('-', ' ')
        print("\"{}\" -- {} views".format(key, v))
    print("                                 ")
  ```
## More Information
* [Joining tables](https://classroom.udacity.com/courses/ud197/lessons/3415228765/concepts/33932188550923)
* [The select ...where statement](https://classroom.udacity.com/courses/ud197/lessons/3423258756/concepts/33885287000923)
* [Select clauses](https://classroom.udacity.com/courses/ud197/lessons/3423258756/concepts/33885287080923)
* [Writing code with DB-API](https://classroom.udacity.com/courses/ud197/lessons/3483858580/concepts/35153985360923)
* [Views](https://classroom.udacity.com/courses/ud197/lessons/b8756d6f-2072-4511-9a46-33579413153d/concepts/f49b275d-c91f-48c6-b3a1-06627323bf03)
* [The select statement](https://www.postgresql.org/docs/9.5/static/sql-select.html)
* [SQL string functions](https://www.postgresql.org/docs/9.5/static/functions-string.html)
* [Aggregate functions](https://www.postgresql.org/docs/9.5/static/functions-aggregate.html)
## Author
* **abdulrahman ali alfaifi**
## Acknowledgments
* Hat tip to anyone whose code was used
* Inspiration
* etc











  