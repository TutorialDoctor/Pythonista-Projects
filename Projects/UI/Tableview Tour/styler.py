import ui

v = ui.load_view()
test = ui.load_view('test')
test2 = ui.load_view('test2')
test3 = ui.load_view('test3')
L = ui.ListDataSource([])

L.highlight_color='#f1f1f1'
L.font=('Baskerville',23)
L.text_color='red'

read=test2['text']


L.items=[
	{'title':'Widgets','image':ui.Image.named('iob:gear_a_32')},
	{'title':'Read','image':ui.Image.named('iob:eye_32')},
	{'title':'Settings','image':ui.Image.named('iob:settings_32')},
	]

def row(sender):
	if sender.selected_row==0:
		nav.push_view(test)
	elif sender.selected_row==1:
		nav.push_view(test2)
	elif sender.selected_row==2:
		nav.push_view(test3)

table=v['Menu']
table.tint_color='green'
table.data_source=L
table.delegate = L
L.action=row
#v.present('sheet')

nav=ui.NavigationView(table)
nav.height=480
nav.width=320
nav.present('sheet',hide_title_bar=True)
