# coding: utf-8
# rethinking logic
view_length = 1024

class Picture():
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y

pic = Picture()

for x in range(1000):
	if pic.x<view_length:
		pic.x+=30
		print (pic.x,pic.y)
	else:
		pic.x=0
		pic.y=pic.y+50
		print (pic.x,pic.y)