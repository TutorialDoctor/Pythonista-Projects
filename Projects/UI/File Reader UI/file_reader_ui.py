# coding: utf-8

import ui,os




view = ui.load_view()

# CLASSES
class MyTableViewDelegate (object):
	def tableview_did_select(self, tableview, section, row):
		# Called when a row was selected.
		cell = tableview.data_source.items[row]
		set_view_text(str(cell))

	def tableview_did_deselect(self, tableview, section, row):
		# Called when a row was de-selected (in multiple selection mode).
		pass

	def tableview_title_for_delete_button(self, tableview, section, row):
		# Return the title for the 'swipe-to-***' button.
		return 'Trash it'


# FUNCTIONS		
def set_view_text(f):
	with open('Files/'+f,'r') as infile:
		main_view = view['main']
		text_view = main_view['textview1']
		text_view.text = infile.read()
		text_view.editable = False

def fill_tableview():
	table = view['side']['tableview1']
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
view.present('fullsceen')


# Regular expressions for search:




# UNUSED CODE
# This function was used for testing
def fill_table():
	table = v['side']['tableview1']
	table_items=['apple','banana','cherry','grape','kiwi']
	list_source = ui.ListDataSource(table_items)
	table.data_source = list_source

# If you want toolbar options
def create_l_buttonItems(*buttons):
	items=[]
	for b in buttons:
		b=ui.ButtonItem(b)
		b.tint_color='#4b4b4b'
		items.append(b)
	return items
#l=create_l_buttonItems('File','Edit','Save')
#view.left_button_items=l

# Can be used as a data source for a more complex app
class MyTableViewDataSource (object):
	def tableview_number_of_sections(self, tableview):
		# Return the number of sections (defaults to 1)
		return 1

	def tableview_number_of_rows(self, tableview, section):
		# Return the number of rows in the section
		return 0

	def tableview_cell_for_row(self, tableview, section, row):
		# Create and return a cell for the given section/row
		cell = ui.TableViewCell()
		cell.text_label.text = 'Foo Bar'
		#return cell
		return os.listdir('.')

	def tableview_title_for_header(self, tableview, section):
		# Return a title for the given section.
		# If this is not implemented, no section headers will be shown.
		#return 'Some Section'
		pass

	def tableview_can_delete(self, tableview, section, row):
		# Return True if the user should be able to delete the given row.
		return True

	def tableview_can_move(self, tableview, section, row):
		# Return True if a reordering control should be shown for the given row (in editing mode).
		return True

	def tableview_delete(self, tableview, section, row):
		# Called when the user confirms deletion of the given row.
		pass

	def tableview_move_row(self, tableview, from_section, from_row, to_section, to_row):
		# Called when the user moves a row with the reordering control (in editing mode).
		pass
