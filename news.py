#!/usr/bin/env python3
from datetime import datetime
import psycopg2


def log_anlys():
    try:
        print('try connecting ...')
        db = psycopg2.connect("dbname=news")
        print("connected successfully")

        # Return the most popular three articles of all time:
        c = db.cursor()
        c.execute("select articles.title, count(path) as views from log,\
                    articles where log.path = '/article/' || articles.slug \
                    group by 1 order by 2 desc limit 3 ")
        sul_1 = c.fetchall()
        for key, v in sul_1:
            print("\"{}\" -- {} views".format(key, v))

        # Return the most popular article authors of all time:
        c = db.cursor()
        c.execute("select authors.name, count(log.path)from articles, authors,\
                    log where articles.author = authors.id and \
                    log.path = '/article/' || articles.slug group by 1 \
                    order by 2 desc")
        sul_2 = c.fetchall()
        for key, v in sul_2:
            print("{} -- {} views".format(key, v))

        # Return on which days did more than 1% of requests lead to errors:
        c = db.cursor()
        c.execute("with reqs as (select Date(time) as date, count(*) from log\
                    group by 1 order by 1),errs as (select Date(time) as date,\
                    count(*)from log where status <> '200 OK' \
                    group by 1 order by 1), err_rate as (select reqs.date, \
                    errs.count::float/reqs.count::float * 100 as err_pct \
                    from reqs,errs where reqs.date = errs.date) \
                    select * from err_rate where err_pct > 1")
        sul_3 = c.fetchall()
        for date, err in sul_3:
            date_str = datetime.strftime(date, '%b %d,%Y')
            print("{} -- {:.1f}% errors".format(date_str, err))
        db.close()

    except psycopg2.DatabaseError, e:
        print("<error message>")


if __name__ == '__main__':

    print('This program is being run by itself')
    log_anlys()
else:
    print('I am being imported from another module')
