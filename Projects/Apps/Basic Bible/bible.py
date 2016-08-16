# coding: utf-8
import ui,sqlite3,datetime,sound,console,clipboard,dialogs,re,objc_util,editor,os

# This script uses 2 tables from the database, but there are others for translations
"""
table_name: t_kjv
	records:
		b - book (int)
		c - chapter (int)
		v - verse (int)
		t - text (str)

table_name: key_english
	records:
		b - book (int)
		n - name (str)

table_name: bible_version_key
		id
		table
		abbreviation
	
American Standard - ASV1901 (ASV)
Bible in Basic English - (BBE)
Darby
King James Version (KJV)
Webster's Bible (WBT)
World English Bible (WEB)
Young's Literal Translation (YLT)
"""

instructions = """
Thoughts can be frozen and unfrozen using the Freeze Switch above.

Use the Thoughts(arrow) button to save a scripture selection to this Thought Bubble.

Uses the Load Button to load old thoughts from your Thoughts File into this Thought Bubble

Use the View Thoughts button to view your old thoughts.

The Save Thoughts button will save your current thoughts to your Thoughts File.

Use the Translate button to set the translation of the bible.

Use the Clip button to save your thoughts to the clipboard.

Use the Share button to share your thoughts via the IOS Share Sheet.
"""

#Used this code to get book number to book name conversion. Much easier than doing a query in two tables.
#con = sqlite3.connect('bible-sqlite.db')
#cur = con.cursor()
#a = cur.execute('select b,n from key_english')
#print(dict([x for x in a]))


# VARIABLES
pairs={1: 'Genesis', 2: 'Exodus', 3: 'Leviticus', 4: 'Numbers', 5: 'Deuteronomy', 6: 'Joshua', 7: 'Judges', 8: 'Ruth', 9: '1 Samuel', 10: '2 Samuel', 11: '1 Kings', 12: '2 Kings', 13: '1 Chronicles', 14: '2 Chronicles', 15: 'Ezra', 16: 'Nehemiah', 17: 'Esther', 18: 'Job', 19: 'Psalms', 20: 'Proverbs', 21: 'Ecclesiastes', 22: 'Song of Solomon', 23: 'Isaiah', 24: 'Jeremiah', 25: 'Lamentations', 26: 'Ezekiel', 27: 'Daniel', 28: 'Hosea', 29: 'Joel', 30: 'Amos', 31: 'Obadiah', 32: 'Jonah', 33: 'Micah', 34: 'Nahum', 35: 'Habakkuk', 36: 'Zephaniah', 37: 'Haggai', 38: 'Zechariah', 39: 'Malachi', 40: 'Matthew', 41: 'Mark', 42: 'Luke', 43: 'John', 44: 'Acts', 45: 'Romans', 46: '1 Corinthians', 47: '2 Corinthians', 48: 'Galatians', 49: 'Ephesians', 50: 'Philippians', 51: 'Colossians', 52: '1 Thessalonians', 53: '2 Thessalonians', 54: '1 Timothy', 55: '2 Timothy', 56: 'Titus', 57: 'Philemon', 58: 'Hebrews', 59: 'James', 60: '1 Peter', 61: '2 Peter', 62: '1 John', 63: '2 John', 64: '3 John', 65: 'Jude', 66: 'Revelation'}

database = 'bible-sqlite.db'
# I'd like to add a timestamp to notes, so:
time_stamp = datetime.datetime.today().strftime('%m_%d_%Y_%H:%M:%S')
# File name for our notes file (here for easy access)
save_file = 'notes.txt'
thoughts_file='thoughts.txt'
translation='t_kjv'


# We will load the following list into a list dialog
translations={"t_asv":"American Standard - ASV1901 (ASV)",
"t_bbe":"Bible in Basic English - (BBE)",
"t_dby":"Darby - (DBY)",
"t_kjv":"King James Version (KJV)",
"t_wbt":"Webster's Bible (WBT)",
"t_web":"World English Bible (WEB)",
"t_ylt":"Young's Literal Translation (YLT)"}
# END VARIABLES

# Try to make a directory named 'Notes.' Do nothing if there is an exception error.
try:
	document_directory = os.mkdir('Notes')
except: None


# CLASSES			
# I will leave the results as a list so that I can load them into a tableview data source
# Textfield
class MyTextFieldDelegate (object):
	def textfield_should_begin_editing(self, textfield):
		return True
	def textfield_did_begin_editing(self, textfield):
		pass
	def textfield_did_end_editing(self, textfield):
		pass
	def textfield_should_return(self, textfield):
		textfield.end_editing()
		return True
	def textfield_should_change(self, textfield, range, replacement):
		return True
	def textfield_did_change(self, textfield):
		try:
			con = sqlite3.connect('bible-sqlite.db')
			cur = con.cursor()			
			substring= textfield.text
			sub_query="select b,c,v,t from {} where t like '%{}%'".format(translation,substring)
			sub_all=[x for x in cur.execute(sub_query)]
			"""
			Leaving for reference, for now.
			b=sub_all[0][0]
			c=sub_all[0][1]
			v=sub_all[0][2]
			t=sub_all[0][3]
			n=[x for x in cur.execute("select n from key_english where b={}".format(b))]
			n=n[0][0]
			"""
			#table.data_source = ui.ListDataSource(re.findall('\s'+textfield.text+'.+',contents.text))
			table.data_source = ui.ListDataSource(sub_all)
			table.reload()
			#table.reload_data()
		except:
			None

#Textview
class MyTextViewDelegate (object):
	def textview_should_begin_editing(self, textview):
		return True
	def textview_did_begin_editing(self, textview):
		pass
	def textview_did_end_editing(self, textview):
		pass
	def textview_should_change(self, textview, range, replacement):
		return True
	def textview_did_change(self, textview):
		return True
	def textview_did_change_selection(self, textview):
		pass

#Tableview
class MyTableViewDelegate (object):
	def tableview_did_select(self, tableview, section, row):
		# Called when a row was selected.
		item = tableview.data_source.items[row]
		search_selection.text =  str(pairs[item[0]])+' '+str(item[1])+': '+str(item[2])+'\n'+str(item[3])

	def tableview_did_deselect(self, tableview, section, row):
		# Called when a row was de-selected (in multiple selection mode).
		pass

	def tableview_title_for_delete_button(self, tableview, section, row):
		# Return the title for the 'swipe-to-***' button.
		return 'Delete'
# END CLASSES


# FUNCTIONS
# closes the superview of the sender
def close(sender):
	sender.superview.close()

# save text in a view to the clipboard
def clip(sender):
	clipboard.set(thoughts.text)
	console.alert('Saved to Clipboard')

# open a list dialog
def translate(sender):
	global translation
	show=dialogs.list_dialog('Translations',[trans for trans in translations])
	translation=show
	try:
		translation_label.text = translations[translation]
	except: None
	
# open the IOS share sheet
def share(sender):
	dialogs.share_text(thoughts.text)

# load sqlite3 query into a tableview as a result of a segmented control action
def test(sender):
	con = sqlite3.connect(database)
	cursor=con.cursor()
	# A query to get all old testament book names in the 'key_english' table 
	ot_query = 'select n from key_english where b < 40'
	ot_bks = [x[0] for x in cursor.execute(ot_query)]
	
	# A query to get all new testament book names in the 'key_english' table 
	nt_query = 'select n from key_english where b >= 40'
	nt_bks = [x[0] for x in cursor.execute(nt_query)]
	
	selected_testament = sender.segments[sender.selected_index]
	
	if selected_testament=='Old Testament':
		books.data_source.items=ot_bks
	
	elif selected_testament=='New Testament':
		books.data_source.items= nt_bks

# Updates the table and text views
def updates(*args):
	# Connect to the sqlite database and create a cursor to query it with
	con = sqlite3.connect(database)
	cursor=con.cursor()
	# Three argument parameters (all tableviews) that were passed in using a lambda function.
	tbl_books = args[0]
	tbl_chapters = args[1]
	control_testaments = args[2]
	
	# A query to get all book names in the 'key_english' table
	all_bks_query = 'select n from key_english'
	all_bks = [x[0] for x in cursor.execute(all_bks_query)]
	
	# Store tableview selections
	selected_book = tbl_books.items[tbl_books.selected_row]
	selected_chap = tbl_chapters.items[tbl_chapters.selected_row]
	#selected_testament = control_testaments.segments[control_testaments.selected_index]
	
	
	# Select book from the key_english table where the name = the selected book/cell of a tableview
	num_query = "select b from key_english where n='{}'".format(selected_book)
	bk_num=[x for x in cursor.execute(num_query)][0][0]
	
	c = selected_chap # unnecessary perhaps but using 'c' is shorter.
	
	# Select chapter,verse,text from the t_kjv table where book = book number (tableview) and chapter = selected chapter
	txt_query = "select c,v,t from '{}' where b = '{}' AND c = '{}'".format(translation,bk_num,c)
	txt = [row for row in cursor.execute(txt_query)]
	# Format the text as -- ''+chapter+text -- ('' can be replaced with whatever prefix you want)
	txt_formatted = "\n".join("{} {}: {}\n".format('',c,t) for b,c,t in txt)
	
	# If the formatted text is an empty string, set the contents textview to a string
	# This is a quick fix if a user selects a chapter in a book that doesn't exist for that book
	if txt_formatted=='':
		contents.text = 'Chapter does not exist'
	
	# Otherwise, set the contents textview to the formatted text
	else: contents.text = txt_formatted
	# Set the heading label to the selected book plus the selected chapter (as a string)
	heading.text=selected_book+' '+str(selected_chap)

#	Save text/selected text in a textview to a file
def save_selection(sender):
	'''saves text/selected text in a textview to a file. If no text is selected, the entire text is saved.'''
	# Get the beginning of the textview selection
	beg= contents.selected_range[0]
	# Get the end of the textview selection
	end = contents.selected_range[1]
	# Get the entire text in the textview
	txt = contents.text
	# If text is selected (if there is a substring from beginning to end)...
	with open('Notes/'+save_file,'a') as outfile:
		if txt[beg:end] != '':
			# write the text to a file with a timestamp, the heading lable text, and the selected text.
			outfile.write('\n'+time_stamp+'\n'+heading.text+'\n\n'+txt[beg:end]+'\n')
		# Otherwise...
		else:
			# write the entire text to the file.
			outfile.write('\n'+time_stamp+'\n'+heading.text+'\n\n'+txt+'\n')
	# Play a sound
	sound.play_effect('ui:switch8')
	# Alert the user that fhe file has been saved to the file.
	console.alert('Saved to {}'.format(save_file))

# Same logic as save_selection
def selectionToThoughts(sender):
	beg= contents.selected_range[0]
	end = contents.selected_range[1]
	txt = contents.text
	if txt[beg:end] != '':
		thoughts.text = thoughts.text +heading.text+'\n'+txt[beg:end]+'\n\n'
	else:
		thoughts.text = thoughts.text +heading.text+'\n'+txt+'\n\n'
	sound.play_effect('rpg:DrawKnife2')

# Save text of a textview to a file
def save_thoughts(sender):
	with open('Notes/'+thoughts_file,'a')	as outfile:
		outfile.write(time_stamp+'\n'+thoughts.text+'\n')
	sound.play_effect('rpg:BookFlip2')
	console.alert('Saved to {}'.format(thoughts_file))

# Make a textview editable or not editable with a switch.
def freeze(sender):
	if sender.value == True:
		thoughts.editable=True
	if sender.value==False:
		thoughts.editable=False

# Load text from a file into the 'thoughts' textview
def load_thoughts(sender):
	with open('Notes/'+thoughts_file,'r') as infile:
		thoughts.text = infile.read()

# Set the 'thoughts' textview to an empty string (clear it).
def clear_thoughts(sender):
	thoughts.text=''

# Creating a quick popup sheet to preview a text file called 'thoughts.txt' (see top)
def view_thoughts(sender):
	v=ui.View(name=thoughts_file)
	v.width=540
	v.height=540
	v.background_color='white'
	tv=ui.TextView()
	tv.width=v.width
	tv.height=v.height
	tv.background_color=''
	tv.editable=False
	tv.font=('Times New Roman',18)
	with open('Notes/'+thoughts_file,'r') as infile:
		tv.text=infile.read()
	v.add_subview(tv)
	v.present('sheet')

# Shows the search window
def show_search(sender):
	def show():
		search.hidden=False
		search.alpha=.9
	ui.animate(show,.4)
	#search.present('sheet')

# Hides the search window
def hide_search(sender):
	def hide():
		search.alpha=0
	ui.animate(hide,.4)
	#search.present('sheet')
	#search.hidden=True

def choose_theme(sender):
	light_themes = [None,'Default','Dawn','Tomorrow','Solarized Light']
	dark_themes = ['Solarized Dark','Cool Glow','Gold','Tomorrow Night','Oceanic','Editorial']
	thm_nm= dialogs.list_dialog('Themes',light_themes+dark_themes)
	if thm_nm in light_themes:
		for x in background_changes:
			x.background_color='#fff'
	elif thm_nm in dark_themes:
		for x in background_changes:
			x.background_color='#373737'
	editor.apply_ui_theme(bible, theme_name=thm_nm)
	
def clear_search(sender):
	search_field.text=''

def forward_to_thoughts(sender):
	thoughts.text = thoughts.text +'\n\n'+search_selection.text
	sound.play_effect('rpg:BookFlip2')

# File name for our thoughts file.
def choose_file():
	global thoughts_file
	file_select= dialogs.list_dialog('Select A File',['New']+os.listdir('Notes'))
	if file_select=='New':
		thoughts_file = dialogs.input_alert('Name your thoughts file')+'.txt'
	elif file_select==None:
		pass
	else:
		thoughts_file= file_select

def view_files(sender):
	global thoughts_file
	file_select= dialogs.list_dialog('Select A File',['New']+os.listdir('Notes'))
	if file_select=='New':
		thoughts_file = dialogs.input_alert('Name your thoughts file')+'.txt'
	elif file_select==None:
		pass
	else:
		thoughts_file= file_select

# END FUNCTIONS

# I think it is okay to use single-letter variable names for small tasks, but certainly not all throughout your code. Comments help here also.


# IMPLEMENTATION
# Getting ui elements and setting actions
bible = ui.load_view()
heading = bible['book_heading']
books = bible['books']
chapters = bible['chapters']
contents = bible['contents']
testaments = bible['testaments']
testaments2 = bible['testaments2']
testaments.action=test
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
save_button = bible['view1']['btn_save']
save_button.action=save_selection
close_button = bible['btn_close']
close_button.action=close
clip_button = bible['view1']['btn_clip']
clip_button.action=clip
translate_button = bible['view1']['btn_translate']
translate_button.action=translate
share_button = bible['view1']['btn_share']
share_button.action=share
search_button = bible['view1']['btn_search']
search_button.action=show_search
search_close_button = bible['search']['btn_close']
search_close_button.action = hide_search
file_button = bible['view1']['btn_file']
file_button.action=view_files
theme_button = bible['btn_theme']
theme_button.action = choose_theme
translation_label = bible['label_translation']
#chapters.data_source = ui.ListDataSource(range(1,100))



# SEARCH ENGINE
search=bible['search']
search.alpha=0
search.hidden=True
search.border_color = 'red'
search.border_width=1
search_field = bible['search']['search_field']
search_field.delegate = MyTextFieldDelegate()
search_clear_button = bible['search']['btn_clear_search']
search_clear_button.action = clear_search
forward_button = search['btn_forward']
forward_button.action= forward_to_thoughts
text = search['textview1']
search_selection = search['textview2']
search_selection.text = """Romans 13: 8
Owe no man any thing, but to love one another: for he that loveth another hath fulfilled the law."""
table= search['tableview1']
table.delegate = MyTableViewDelegate()
# END SEARCH ENGINE

background_changes=[search_selection,search,books,contents,bible,thoughts,bible['view1'],heading,close_button,theme_button]
for x in background_changes:
	x.background_color='#fff'


thoughts.text = instructions

# This lambda function is what allows me to pass arguments to a view's action function. This function is what makes it all work.
f = lambda sender: updates(sender,chapters.data_source,testaments)

# Quick and dirty query to preload a tableview with an sqlite record.
books.data_source.items = [x[0] for x in sqlite3.connect('bible-sqlite.db').execute('select n from key_english')]
books.data_source.action = f

choose_file()
# Display the bible witha hidden title bar and restrict its orientation to landscape.
bible.present(orientations=['landscape'],hide_title_bar=True)


