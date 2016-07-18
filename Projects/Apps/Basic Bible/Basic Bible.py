import ui,sqlite3,datetime,sound,console

time_stamp = datetime.datetime.today().strftime('%m_%d_%Y_%H:%M:%S')
save_file = 'notes.txt'
thoughts_file = 'thoughts.txt'

def updates(*args):
	con = sqlite3.connect('bible-sqlite.db')
	cursor=con.cursor()
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
	
	c = selected_chap
	
	txt_query = "select c,v,t from 't_kjv' where b = '{}' AND c = '{}'".format(bk_num,c)
	txt = [row for row in cursor.execute(txt_query)]
	txt_formatted = "\n".join("{} {}: {}\n".format('',c,t) for b,c,t in txt)
	
	if txt_formatted=='':
		contents.text = 'Chapter does not exist'
	
	else: contents.text = txt_formatted
	heading.text=selected_book+' '+str(selected_chap)

def save_selection(sender):
	beg= contents.selected_range[0]
	end = contents.selected_range[1]
	txt = contents.text
	with open(save_file,'a') as outfile:
		if txt[beg:end] != '':
			outfile.write('\n'+time_stamp+'\n'+heading.text+'\n\n'+txt[beg:end]+'\n')
		else:
			outfile.write('\n'+time_stamp+'\n'+heading.text+'\n\n'+txt+'\n')
	sound.play_effect('ui:switch8')
	console.alert('Saved to {}'.format(save_file))

def selectionToThoughts(sender):
	beg= contents.selected_range[0]
	end = contents.selected_range[1]
	txt = contents.text
	if txt[beg:end] != '':
		thoughts.text = thoughts.text +heading.text+'\n'+txt[beg:end]+'\n\n'
	else:
		thoughts.text = thoughts.text +heading.text+'\n'+txt+'\n\n'
	sound.play_effect('rpg:DrawKnife2')

def save_thoughts(sender):
	with open(thoughts_file,'a')	as outfile:
		outfile.write(time_stamp+'\n'+thoughts.text+'\n')
	sound.play_effect('rpg:BookFlip2')
	console.alert('Saved to {}'.format(thoughts_file))

def freeze(sender):
	if sender.value == True:
		thoughts.editable=True
	if sender.value==False:
		thoughts.editable=False

def load_thoughts(sender):
	with open(thoughts_file,'r') as infile:
		thoughts.text = infile.read()

def clear_thoughts(sender):
	thoughts.text=''

def view_thoughts(sender):
	v=ui.View()
	v.width=540
	v.height=540
	v.background_color='white'
	tv=ui.TextView()
	tv.width=v.width
	tv.height=v.height
	tv.background_color=''
	tv.editable=False
	tv.font=('Times New Roman',18)
	with open(thoughts_file,'r') as infile:
		tv.text=infile.read()
	v.add_subview(tv)
	v.present('sheet')


# IMPLEMENTATION
bible = ui.load_view()
heading = bible['book_heading']
books = bible['books']
chapters = bible['chapters']
contents = bible['contents']
testaments = bible['testaments']
thoughts = bible['view1']['thought_bubble']
thoughts_switch = bible['view1']['switch']
thoughts_switch.action = freeze
thoughts_button = bible['view1']['btn_thoughts']
thoughts_button.action = selectionToThoughts
thoughts_save_button = bible['view1']['btn_save_thoughts']
thoughts_save_button.action = save_thoughts
load_button = bible['view1']['btn_load']
load_button.action = load_thoughts
clear_button = bible['view1']['btn_clear']
clear_button.action=clear_thoughts

with open('instructions.txt','r') as infile:
	thoughts.text = infile.read()
	
save_button = bible['view1']['btn_save']
save_button.action=save_selection
f = lambda sender: updates(sender,chapters.data_source,testaments.data_source)
books.data_source.items = [x[0] for x in sqlite3.connect('bible-sqlite.db').execute('select n from key_english')]
books.data_source.action = f
bible.present(orientations=['landscape'])

