import ui,scene,os,console

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
		pass
	def textview_did_change_selection(self, textview):
		pass

class MyTextFieldDelegate (object):
	def textfield_should_begin_editing(self, textfield):
		return True
	def textfield_did_begin_editing(self, textfield):
		pass
	def textfield_did_end_editing(self, textfield):
		if textfield.name =='field':
			if not textfield.text =='':
				text.text += '\n\n'+'Q: '+textfield.text+'?'
			textfield.text=''
		elif textfield.name=='field2':
			if not textfield.text=='':
				text.text += '\n\n'+'A: '+textfield.text+'.'
			textfield.text=''
		elif textfield.name=='field3':
			if not textfield.text=='':
				text.text += '\n\n'+'C: '+textfield.text+'.'
			textfield.text=''
	def textfield_should_return(self, textfield):
		textfield.end_editing()
		return True
	def textfield_should_change(self, textfield, range, replacement):
		return True
	def textfield_did_change(self, textfield):
		pass

class MyTableViewDelegate (object):
	def tableview_did_select(self, tableview, section, row):
		# Called when a row was selected.
		pass

	def tableview_did_deselect(self, tableview, section, row):
		# Called when a row was de-selected (in multiple selection mode).
		pass

	def tableview_title_for_delete_button(self, tableview, section, row):
		# Return the title for the 'swipe-to-***' button.
		return 'Delete'

class MyWebViewDelegate (object):
	def webview_should_start_load(self, webview, url, nav_type):
		return True
	def webview_did_start_load(self, webview):
		pass
	def webview_did_finish_load(self, webview):
		pass
	def webview_did_fail_load(self, webview, error_code, error_msg):
		pass

class MyScrollViewDelegate (object):
	def scrollview_did_scroll(self, scrollview):
		# You can use the content_offset attribute to determine the current scroll position
		pass

v = ui.load_view()
v.name='Noted'
v.tint_color='white'
field = v['field']
field.delegate=MyTextFieldDelegate()
field2 = v['field2']
field2.delegate=MyTextFieldDelegate()
field3 = v['field3']
field3.delegate=MyTextFieldDelegate()
text = v['text']
v.present(title_bar_color='#6ba6cb',title_color='white')
