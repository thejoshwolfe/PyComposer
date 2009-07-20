

class Chord:
    def __init__(self, name, tension=None):
        self.name = name
        self.tension = tension

    def __str__(self):
        rtnStr = "%s chord" % self.name
        if self.tension != None:
            rtnStr += " tension=" + str(self.tension)
        return rtnStr

