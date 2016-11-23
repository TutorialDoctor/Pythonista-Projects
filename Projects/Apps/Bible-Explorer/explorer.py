#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,shutil,sys,csv,ui

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
		text.text=get_table_data(tableItem=-7,entry=int(textfield.text))
	def textfield_should_return(self, textfield):
		textfield.end_editing()
		return True
	def textfield_should_change(self, textfield, range, replacement):
		return True
	def textfield_did_change(self, textfield):
		pass



os.chdir('CSV')

csv_files=['BookAliases.csv', 'Books.csv', 'CrossRefIndex.csv', 'MainIndex.csv', 'People.csv', 'PeopleAliases.csv', 'PeopleCorrections.csv', 'PeopleGenderCorrections.csv', 'PeopleGroups.csv', 'PeopleRelationships.csv', 'PlaceAliases.csv', 'PlaceMarks.csv', 'Places.csv', 'Strongs.csv', 'StrongsIndex.csv', 'TopicIndex.csv', 'Topics.csv', 'Verses.csv', 'VizableBible.csv', 'Writers.csv']

v=ui.load_view()
table=v['table']
table.row_height=200
tables = v['tables']
tables.data_source=ui.ListDataSource(csv_files)
#table.data_source = 

def getAllFileContents():
	for file in csv_files:
		with open(file,'r',encoding='utf-8') as csvfile:
			reader = csv.reader(csvfile)
			return list(reader)
			#return [row for row in reader]

def getFileContents(file):
	with open(file,'r', encoding='utf-8') as csvfile:
		reader = csv.reader(csvfile)
		return list(reader)
		#return [row for row in reader]

def get_table_data(tableItem,entry):
	head = getFileContents(csv_files[tableItem])[0]
	item = getFileContents(csv_files[tableItem])[entry]
	dictionary= dict(zip(head,item))
	table.data_source = ui.ListDataSource(getFileContents(csv_files[tableItem]))
	table.data_source.number_of_lines=7
	#print(dictionary['StrongsID'])
	pretty='\n'.join([x + ' = ' + dictionary[x] for x in head])
	return pretty

text = v['text']
text2 = v['text2']
text2.delegate=MyTextFieldDelegate()
text.text=get_table_data(tableItem=-7,entry=3)
print(get_table_data(3,6))

v.present()
