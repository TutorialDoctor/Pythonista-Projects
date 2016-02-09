# coding: utf-8

import ui

def connect(sender):
	try:
		main.navigation_view.push_view(ui.load_view('Views/'+sender.title))
	except:
		None

main = ui.load_view()
nav = ui.NavigationView(main)
nav.height=main.height
nav.width=main.width
nav.present('sheet',title_bar_color='#bfd6e5')

# text quality is degraded because scaling affects quality, an issue I don't like with Pythonista.
# lines 11 and 12 are where the view is scaled.

for item in main.subviews:
	item.action = connect