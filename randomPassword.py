#!/usr/bin/python

import MySQLdb
from hashlib import md5
from string import ascii_uppercase,ascii_lowercase,digits
from random import randint

chars = ascii_uppercase + ascii_lowercase + digits  # Alphanumeric characters

def random_string():            # Random String Generator
    l = [ chars[randint(0,len(chars)-1)] for i in range(5)]
    return ''.join(l)

new_password = random_string()
new_password = md5(new_password).hexdigest()        # Hashing the password using md5

db = MySQLdb.connect(user='root',passwd='password',host='localhost',db='delta')
sql = "UPDATE login SET passwd =%s where user ='root' "
c = db.cursor()
args = (new_password,)
c.execute(sql,args)
db.commit()

db.close()
