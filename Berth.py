class Berth(object):

	def __init__(self, berth, ypos, xpos):
		self.berth = str(berth)
		self.ypos = int(ypos)
		self.xpos = int(xpos)
		
		self.desc = '----'

	def setDesc(self, desc):
		self.desc = str(desc)

	def showBerth(self): #<for testing
		self.desc = self.berth

