
from midi.MidiOutFile import MidiOutFile

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
        offsetIntoMode = (note.number - 1) % 7 + 1
        octaveOffset = 12 * (offsetIntoMode - note.number) / 7
        return self.key + octaveOffset + self.mode[offsetIntoMode - 1]
    
    def getEventTracks(self):
        """
        convert notes to on- and off-events
        """
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
            positions = track.notes.keys()
            positions.sort()
            for pos in positions:
                noteArray = track.notes[pos]
                for note in noteArray:
                    addEvent(pos, Event(note, "on")) # TODO on/off
                    addEvent(pos + note.duration, Event(note, "off")) # TODO on/off
            eventTracks.append(events)
        return eventTracks
    
    def writeToMidi(self, filepath, eventTracks=None):        
        if eventTracks == None:
            eventTracks = self.getEventTracks()

        midi = MidiOutFile(filepath)
        midi.header(1, len(self.tracks), 480) # TODO 480?
        
        for i in range(len(self.tracks)):
            track = self.tracks[i]
            events = eventTracks[i]
            midi.start_of_track(i)
            midi.tempo(60000000 / self.tempo) # int(60,000,000.00 / BPM)
            midi.time_signature(self.beatsPerMeasure, 2, 24, 8) # TODO: ?
            
            midi.patch_change(i, track.instrument)
            
            lastPos = 0
            positions = events.keys()
            positions.sort()
            for pos in positions:
                eventArray = events[pos]
                deltaPos = pos - lastPos
                midiTime = int(float(deltaPos) * 300) # TODO: wtf
#                print "----- " + str(pos) + " -----"
                for event in eventArray:
                    midi.update_time(midiTime)
                    pitch = self.noteToPitch(event.note)
                    if event.type == "on": # TODO on/off
#                        print str(pitch) + " on"
                        midi.note_on(channel=i, note=pitch)
                    else:
#                        print str(pitch) + " off"
                        midi.note_off(channel=i, note=pitch)
                    midiTime = 0 # remainder of events are simultaneous
                lastPos = pos
            midi.update_time(0)
            midi.end_of_track()
        midi.eof()





























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


