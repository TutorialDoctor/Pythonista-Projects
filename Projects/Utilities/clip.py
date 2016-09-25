with open('dictionary.json','r',encoding='utf-8') as infile:
	with open('copy.json','w',encoding='utf-8') as outfile:
		outfile.write(infile.read())
