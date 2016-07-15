import ui,sqlite3
<<<<<<< HEAD
=======
#db='bible-sqlite'
#connection = sqlite3.connect(db+'.db')
#cursor = connection.cursor()
>>>>>>> origin/master


def updates(*args):
	con = sqlite3.connect('bible-sqlite.db')
	cursor=con.cursor()
<<<<<<< HEAD
	tbl_books = args[0]
	tbl_chapters = args[1]
	tbl_testaments = args[2]
	
	all_bks_query = 'select n from key_english'
	all_bks = [x[0] for x in cursor.execute(all_bks_query)]
	
	ot_query = 'select n from key_english where b < 40'
	ot_bks = [x[0] for x in cursor.execute(ot_query)]
	
	nt_query = 'select n from key_english where b > 40'
	nt_bks = [x[0] for x in cursor.execute(nt_query)]
	
	tbl_books.items = all_bks
	selected_book = tbl_books.items[tbl_books.selected_row]
	selected_chap = tbl_chapters.items[tbl_chapters.selected_row]
	selected_testament = tbl_testaments.items[tbl_testaments.selected_row]

	#if selected_testament=='Old Testament':
		#tbl_books.items=ot_bks
	
	#elif selected_testament=='New Testament':
		#tbl_books.items= nt_bks

	num_query = "select b from key_english where n='{}'".format(selected_book)
	bk_num=[x for x in cursor.execute(num_query)][0][0]
=======
	selected_book = args[0].items[args[0].selected_row]
	selected_chap = args[1].items[args[1].selected_row]
	
	
	num_query = "select b from key_english where n='{}'".format(selected_book)
	bk_num=[x for x in cursor.execute(num_query)][0][0]
	print(bk_num)
>>>>>>> origin/master
	
	c = selected_chap
	
	txt_query = "select c,v,t from 't_kjv' where b = '{}' AND c = '{}'".format(bk_num,c)
	txt = [row for row in cursor.execute(txt_query)]
<<<<<<< HEAD
	txt_formatted = "\n".join("{} {}: {}\n".format('*',c,t) for b,c,t in txt)
	
	if txt_formatted=='':
		contents.text = 'Chapter does not exist'
	
	else: contents.text = txt_formatted
	heading.text=selected_book+' '+str(selected_chap)

=======
	txt_formatted = "\n".join("{} {}: {}\n".format(bk_num,c,t) for b,c,t in txt)
	contents.text = txt_formatted
	heading.text=selected_book+' '+str(selected_chap)
	

f = lambda sender: updates(sender,chapters.data_source)
>>>>>>> origin/master

# Implementation
bible = ui.load_view()
heading = bible['book_heading']
books = bible['books']
chapters = bible['chapters']
contents = bible['contents']
<<<<<<< HEAD
testaments = bible['testaments']
#books.data_source = ui.ListDataSource(l)
#books.data_source.items = l
f = lambda sender: updates(sender,chapters.data_source,testaments.data_source)
books.data_source.items = [x[0] for x in sqlite3.connect('bible-sqlite.db').execute('select n from key_english')]
books.data_source.action = f
=======

books.data_source.action = f

>>>>>>> origin/master
bible.present(orientations=['landscape'])
