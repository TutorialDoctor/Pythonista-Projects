# coding: utf-8
# By the Tutorial Doctor 1/29/16

import ui,os

# FUNCTIONS
def btn_action1(sender):
	def connect(a,b):
		if sender.title == a:
			view_to_push = b
			pushed_view = ui.load_view(view_to_push)
			v.navigation_view.push_view(pushed_view)
		
			if sender.title == 'Web':
				web = pushed_view['webview1']
				with open('Files/index.html','r') as infile:
					web.load_html(infile.read())
			if sender.title=='File':
				table=pushed_view['view1']['tableview1']
				table_items = os.listdir('./Files')
				# You can use a list or a class as the data source for the tableview
				list_source = ui.ListDataSource(table_items)
				table.data_source = list_source
	
	connect('File','file_view')
	connect('Edit','edit_view')
	connect('Tools','toolbar')
	connect('Web','webview')


def create_l_buttonItems(*buttons):
	items=[]
	for b in buttons:
		b=ui.ButtonItem(b)
		b.tint_color='#494949'
		b.action= btn_action1
		items.append(b)
	return items


# SETUP
v = ui.View()
v.name='Main'
v.background_color='white'
t = ui.TextView()
t.width=768
t.height=768
t.font=('Avenir Light',16)
with open('Files/tutorial.txt','r') as infile:
	t.text=infile.read()
v.add_subview(t)


# IMPLEMENTATION
l = create_l_buttonItems('File','|','Edit','|','Tools','|','Web')
v.left_button_items = l
nav = ui.NavigationView(v)
nav.present()