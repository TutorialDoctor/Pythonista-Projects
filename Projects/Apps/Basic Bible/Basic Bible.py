# coding: utf-8
import sqlite3,ui

# http://simoncozens.github.io/open-source-bible-data/
# https://github.com/scrollmapper/bible_databases
# #http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html

# f-strings?

databases = ['kjv.db','bible-sqlite']
con = sqlite3.connect(databases[0])
cursor = con.cursor()

bible = ui.load_view('Basic Bible')
content=bible['content']

l = [row for row in cursor.execute("select book,chapter,content from 'bible' where book = 'Rom' AND chapter = '12'")]

s = "\n".join("{} {}: {}\n".format(book,chapter,content) for book,chapter,content in l)

content.text = s

bible.present()







# ADDITIONAL HELPER CODE

#all_tables()
#all_in_table()
#book(('Gen',))

# Useful
#for row in cursor.execute("select book,chapter,content,verse from 'bible' where book = 'Rev'"):
	#print(row)

#cursor.execute("SELECT * FROM sqlite_master")

def all_in_table():
	for row in cursor.execute("SELECT * FROM bible"):
		print(row)

def all_tables():
	for row in cursor.execute("SELECT name FROM sqlite_master WHERE type='table';"):
		print(row)	

def stuff():
	for row in cursor.execute('select * from sqlite_master'):
		print(row)

def book(x):
	for row in cursor.execute("select * from bible where book='?'",x):
		print(row)



def get_info():
	return [row for row in cursor.execute("select book,chapter,verse,content from 'bible' where book = 'Jonah' ")]

#print(get_info())
# A list of 2-Tuples. (Book,Chapter,Verse,Content)

def get_content():
		return [row for row in cursor.execute("select content from 'bible' where book = 'Jonah' ")]
		

