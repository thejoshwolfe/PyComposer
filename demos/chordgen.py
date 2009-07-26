# create a random chord progression and render it into a midi using
# an acoustic grand piano

from midi.MidiOutFile import MidiOutFile
from composer import composer
import os

from composer.note import normalize

def putInScale(note):
    scale = (0, 2, 4, 5, 7, 9, 11)
    norm = normalize(note.number)
    return ((note.number - norm) / 7) * 12 + scale[norm-1]

def noteToMidi(note):
    return 0x40+putInScale(note)

def addChord(chord):
    for note in chord.notes:
        midi.update_time(0)
        midi.note_on(channel=0, note=noteToMidi(note))

    midi.update_time(192*4)
    for note in chord.notes:
        midi.note_off(channel=0, note=noteToMidi(note))
        midi.update_time(0)

# grab a chord progression
progression = composer.chordGen()

out_file = 'out.mid'

midi = MidiOutFile(out_file)

midi.header(0, 1, 480)
midi.start_of_track()
midi.tempo(750000)
midi.time_signature(4, 2, 24, 8)


for chord in progression:
    addChord(chord)
    
midi.update_time(0)
midi.end_of_track()

midi.eof() # currently optional, should it do the write instead of write??


os.system('timidity %s' % out_file)

