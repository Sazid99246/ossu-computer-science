import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

#Setting up the tables
#Drop existing tables if any
#Create new tables accordingly

cur.executescript('''

DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Course (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE 
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)   
);
''')

fname = input("Enter file name: ")
if len(fname) < 1 : fname = 'roster_data.json'

# file format
# [
#   [
#     "Dulcie",
#     "si110",
#     1
#   ],

str_data  = open(fname).read()      #open and read file
json_data = json.loads(str_data)    #Take str_data strings in return json objects

#Extracting name and title from json_data
for entry in json_data:
    name = entry[0];
    title = entry[1];
    role = entry[2];
    print((name, title, role))

#Start writing our data into our database
    cur.execute(''' INSERT OR IGNORE INTO User (name)
        VALUES  (?)''', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    cur.execute(''' INSERT OR IGNORE INTO Course (title)
        VALUES (?)''', (title,))
    cur.execute('SELECT id FROM Course WHERE title =?', (title,))
    course_id = cur.fetchone()[0]

    cur.execute(''' INSERT OR REPLACE INTO Member (user_id, course_id, role)
        VALUES (?, ?, ?)''', (user_id, course_id, role))
conn.commit()