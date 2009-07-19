
from chord import Chord

chords = {}

def addChord(chord):
	chords[chord.name] = chord

addChord(Chord.new( "1", tension=0  ))
addChord(Chord.new( "2", tension=12 ))
addChord(Chord.new( "3", tension=6  ))
addChord(Chord.new( "4", tension=2  ))
addChord(Chord.new( "5", tension=3  ))
addChord(Chord.new( "6", tension=6  ))
addChord(Chord.new( "7", tension=60 ))




