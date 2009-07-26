
major = [0, 2, 4, 5, 7, 9, 11]
minor = [0, 2, 3, 5, 7, 8, 10]

class Song:
    def __init__(self):
        self.tracks = []
        self.tempo = 140 # BPM
        self.beatsPerMeasure = 4
        self.key = 0x40
        self.mode = major
    
    def addTrack(self, track):
        self.tracks.append(track)
    
    def noteToPitch(self, note):
        """
        returns the midi pitch (int) for a note in the current key and mode
        """
        offsetIntoMode = ((note.number - 1) % 7) + 1
        octaveOffset = 12 * (offsetIntoMode - note.number) / 7
        return self.key + octaveOffset + self.mode[offsetIntoMode]
    
    def writeToMidi(self, filepath):
        # convert notes to on- and off-events
        ON, OFF = range(2)
        class Event:
            def __init__(self, note, type):
                self.note = note
                self.type = type
        eventTracks = []
        for track in self.tracks:
            events = {}
            def addEvent(pos, event):
                if not events.has_key(pos):
                    events[pos] = []
                events[pos].append(event)
            for pos, noteArray in track.notes.items():
                for note in noteArray:
                    addEvent(pos, Event(note, ON))
                    addEvent(pos + note.duration, Event(note, OFF))
            eventTracks.append(events)
        return eventTracks
    
    def __str__(self):
        return ",".join([str(t) for t in tracks])



#from .track import Track
#from .note import Note

#s = Song()
#t = Track()
#s.addTrack(t)
#t.addNote(0, Note(1))
#t.addNote(1, Note(2))
#t.addNote(2, Note(3))

#eventTracks = s.writeToMidi("")

#print eventTracks


