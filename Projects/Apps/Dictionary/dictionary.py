import json,ui

class MyTextFieldDelegate (object):
	def textfield_should_begin_editing(self, textfield):
		return True
	def textfield_did_begin_editing(self, textfield):
		pass
	def textfield_did_end_editing(self, textfield):
		with open('dictionary.json',encoding='utf-8') as infile:
			data = json.load(infile)
			try:
				txt_definition.text=data[textfield.text.upper()]
			except: None
	def textfield_should_return(self, textfield):
		#textfield.end_editing()
		return True
	def textfield_should_change(self, textfield, range, replacement):
		return True
	def textfield_did_change(self, textfield):
		pass


# A JSON representation of Webster's Unabridged Dictionary

v=ui.load_view('dictionaryUI')
fld_word = v['fld_word']
fld_word.delegate = MyTextFieldDelegate()
txt_definition = v['txt_definition']
v.present()

