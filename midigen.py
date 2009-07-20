
# http://www.sonicspot.com/guide/midifiles.html

def int2str(i):
	return chr(i >> 24 & 0xFF) + chr(i >> 16 & 0xFF) + chr(i >> 8 & 0xFF) + chr(i >> 0 & 0xFF)

def short2str(i):
	return chr(i >> 8 & 0xFF) + chr(i >> 0 & 0xFF)


midistr = ""

# header
midistr += "MThd"             # chunk ID
midistr += int2str(6)         # chunk size
midistr += short2str(0)       # format type
midistr += short2str(1)       # number of tracks
midistr += short2str(0x01E0)  # time division


# track 1 (the only track)
trackstr = ""


midistr += "MTrk"                 # track ID
midistr += int2str(len(trackstr)) # chunk size
midistr += trackstr

midifile = open("out.midi", "w")
midifile.write(midistr)
midifile.close()


