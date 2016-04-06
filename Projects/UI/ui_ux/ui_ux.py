# coding: utf-8
import ui

def close(sender):
	window.close()

views = [None,'iPad_infoPage','iPhone_list','ipad_codeEditor','iPad_envelopes']
item = 4

#images
a = ui.Image().named('iob:ios7_contact_outline_256')
x = ui.Image().named('iob:ios7_close_256')
person = ui.Image.named('iob:ios7_people_256')
envelope=ui.Image().named('iob:email_256')
window = ui.load_view(views[item])


#iPhone_list
try:
	scroll = window['scrollview']
	for x in scroll.subviews:
		x['imageview1'].image=a
except:
	None

window.present(hide_title_bar=True,orientations=['portrait'])




#ui.View now supports setting arbitrary attributes, so you don't have to subclass in order to attach some auxiliary data to a view (or any subclass of ui.View). Note that this might hide bugs/typos in your code because something like my_view.fame = ... (instead of my_view.frame) no longer throws an exception (but this is consistent with the way most objects in Python work).

#The UI editor now supports setting custom attributes for views. You can use this to attach arbitrary data to a view or to set built-in attributes that aren't supported directly in the UI editor's inspector (e.g. ui.TextField.keyboard_type).