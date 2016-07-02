# coding: utf-8
import sqlite3,ui,sound

# http://simoncozens.github.io/open-source-bible-data/
# https://github.com/scrollmapper/bible_databases
# #http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
# v.action = lambda sender: myfunc("foo", sender, "bar", something=42)

# f-strings? @ccc posted about this on the forums.

database = ['kjv.db','bible-sqlite']
con = sqlite3.connect(database[0])
cursor = con.cursor()


class Query:
	def get_chapter(sender):
		sound.play_effect('ui:rollover2')
		return chapters.data_source.items[sender.selected_row]

	def get_testament(sender):
		sound.play_effect('ui:rollover2')
		return testaments.data_source.items[sender.selected_row]

	def get_book(sender):
		sound.play_effect('ui:rollover2')
		return books.data_source.items[sender.selected_row]

def activate_table(tbl,src,act):
	li = ui.ListDataSource(src)
	tbl.data_source = li
	tbl.data_source.action = act
	tbl.delegate = li


bible = ui.load_view('Basic Bible')
contents=bible['contents']

chapters = bible['chapters']
books= bible['books']
testaments = bible['testaments']


chapter_src = [i for i in range(1,21)]
activate_table(chapters,chapter_src,Query.get_chapter)

testament_src = ['Old Testament','New Testament']
activate_table(testaments,testament_src,Query.get_testament)

book_src = ['Book','Book','Book','Romans']
activate_table(books,book_src,Query.get_book)


def scripture(book,chapter):
	sql = "select book,chapter,content from 'bible' where book = '{}' AND chapter = '{}'".format(book,chapter)
	l = [row for row in cursor.execute(sql)]
	s = "\n".join("{} {}: {}\n".format(book,chapter,content) for book,chapter,content in l)
	return s

contents.text = scripture('Rom','2')

bible.present(orientations=['landscape'])
























# ADDITIONAL HELPER CODE
# Text Reader Code


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


