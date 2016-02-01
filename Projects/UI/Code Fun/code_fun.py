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
# This is a shorter/better version of a text reader/editor
def set_view_text(f):
	with open('Files/'+f,'r') as infile:
		text_view = main['view1']['textview1']
		text_view.text = infile.read()
		text_view.editable = False
def action(sender):
	sound.play_effect('ui:rollover2')
	set_view_text(table.data_source.items[sender.selected_row])

table = main['view1']['tableview1']
table_items = os.listdir('./Files')
list_source = ui.ListDataSource(table_items)
table.data_source = list_source
table.data_source.action = action
table.delegate=list_source
# End Text Reader Code
