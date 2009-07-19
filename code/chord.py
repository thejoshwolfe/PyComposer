

class Chord:
	def new(name, tension=None):
		chord = Chord()
		chord.name = name
		chord.tension = tension
		
		return chord

	def __str__(self):
		rtnStr = ""
		rtnStr += self.name + " chord"
		if self.tension != None:
			rtnStr += " tension=" + str(self.tension)
		return rtnStr

