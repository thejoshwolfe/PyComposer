

class Track:
    def __init__(self):
        self.notes = {}
        self.instrument = 1 # piano
    

    def addNote(self, pos, note):
        if not self.notes.hasKey(pos):
            self.notes[pos] = []
        self.notes[pos].append(note)


