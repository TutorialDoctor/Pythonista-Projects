# coding: utf-8
import ui,os

# CLASSES
# The main.pyui view inherits this custom class
class ViewClass(ui.View):
	def __init__(self):
		pass
	def touch_began(self,touch):
		def animation():
			panel.alpha=0
		ui.animate(animation,.3)
	def touch_moved(self,touch):
		pass
	def touch_ended(self,touch):
		pass

# FUNCTIONS
def create_buttonItems(*buttons):
	items=[]
	for b in buttons:
		b=ui.ButtonItem(b)
		b.tint_color='#5590ff'
		items.append(b)
	return items

def anim_alpha(sender):
	def animation():
		panel.alpha=1
	ui.animate(animation,.3)

def show_docs(sender):
	doc_view.present(animated=False)

def set_button_images(*x):
	i=0
	while i < len(btns):
		images=x
		btns[i].image = ui.Image().named(images[i])
		i+=1

def set_view_text(f):
	with open('Files/'+f,'r') as infile:
		text_view = main['view1']['textview1']
		text_view.text = infile.read()
		text_view.editable = False

# SETUP
main=ui.load_view('Views/main')
main.left_button_items= create_buttonItems('File')
main.right_button_items= create_buttonItems('Back')
text = main['textview1']
#text.touch_enabled = False
btns = main['view2'].subviews
btns[2].action=anim_alpha
btns[0].action= show_docs
panel = main['view1']
panel.alpha=0

set_button_images('iob:navicon_32','iob:ios7_plus_empty_256','iob:forward_32')

#Reader
doc_view = ui.load_view('Views/docs')
table = doc_view['tableview1']
table_items = os.listdir('./Files')
list_source = ui.ListDataSource(table_items)
table.data_source = list_source
# End Text Reader Code

main.present(animated=False)