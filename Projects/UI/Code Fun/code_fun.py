# coding: utf-8
import ui,os,sound

# Functions
def show_sheet(sender):
	sound.play_effect('ui:click3')
	sheet.present('sheet',title_bar_color='#29a6f6')

def open_main(sender):
	sound.play_effect('ui:click3')
	sheet.close()
	sheet.wait_modal()
	main.present()
	with open('Files/main_text.txt','r') as infile:
		main['view1']['textview1'].text = infile.read()
	main['textview1']

def create_r_buttonItems(*buttons):
	items=[]
	for b in buttons:
		b=ui.ButtonItem(b)
		b.tint_color='white'
		items.append(b)
	return items

# Setup
welcome = ui.load_view('Views/welcome')
main=ui.load_view('Views/main')
im_view = welcome['imageview1']
im_view.image = ui.Image().named('Images/logo.PNG')
sheet = ui.load_view('Views/sheet')
sheet.tint_color='white'
with open('Files/agenda.txt','r') as infile:
	sheet['textview1'].text = infile.read()
sheet.right_button_items= create_r_buttonItems('>')
welcome.present(hide_title_bar=True)
btn = welcome['button1']
btn.action = show_sheet
sheet.right_button_items[0].action = open_main
# All code above this line is pretty much all that was needed to make this GUI function. This code is intentionally long-winded for clarity. 









# Text Reader Code
# CLASSES
class MyTableViewDelegate (object):
	def tableview_did_select(self, tableview, section, row):
		# Called when a row was selected.
		cell = tableview.data_source.items[row]
		set_view_text(str(cell))
		sound.play_effect('ui:rollover2')


	def tableview_did_deselect(self, tableview, section, row):
		# Called when a row was de-selected (in multiple selection mode).
		pass

	def tableview_title_for_delete_button(self, tableview, section, row):
		# Return the title for the 'swipe-to-***' button.
		return 'Trash it'


# FUNCTIONS		
def set_view_text(f):
	with open('Files/'+f,'r') as infile:
		text_view = main['view1']['textview1']
		text_view.text = infile.read()
		text_view.editable = False

def fill_tableview():
	table = main['view1']['tableview1']
	table.delegate = MyTableViewDelegate()
	# Get a list of files in the 'Files' directory
	# You can use any directory relative to the current directory
	table_items = os.listdir('./Files')
	
	# You can use a list or a class as the data source for the tableview
	list_source = ui.ListDataSource(table_items)
	#class_source = MyTableViewDataSource()
	# I will use a list
	table.data_source = list_source

# IMPLEMENTATION
fill_tableview()
# End Text Reader Code