import ui,sqlite3
#db='bible-sqlite'
#connection = sqlite3.connect(db+'.db')
#cursor = connection.cursor()


def updates(*args):
	con = sqlite3.connect('bible-sqlite.db')
	cursor=con.cursor()
	selected_book = args[0].items[args[0].selected_row]
	selected_chap = args[1].items[args[1].selected_row]
	
	
	num_query = "select b from key_english where n='{}'".format(selected_book)
	bk_num=[x for x in cursor.execute(num_query)][0][0]
	print(bk_num)
	
	c = selected_chap
	
	txt_query = "select c,v,t from 't_kjv' where b = '{}' AND c = '{}'".format(bk_num,c)
	txt = [row for row in cursor.execute(txt_query)]
	txt_formatted = "\n".join("{} {}: {}\n".format(bk_num,c,t) for b,c,t in txt)
	contents.text = txt_formatted
	heading.text=selected_book+' '+str(selected_chap)
	

f = lambda sender: updates(sender,chapters.data_source)

# Implementation
bible = ui.load_view()
heading = bible['book_heading']
books = bible['books']
chapters = bible['chapters']
contents = bible['contents']

books.data_source.action = f

bible.present(orientations=['landscape'])
