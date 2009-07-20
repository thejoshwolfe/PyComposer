
# http://www.sonicspot.com/guide/midifiles.html

def int2ba(i):
	return [i >> 24 & 0xFF, i >> 16 & 0xFF, i >> 8 & 0xFF, i >> 0 & 0xFF]

def short2ba(i):
	return [i >> 8 & 0xFF, i >> 0 & 0xFF]

def str2ba(s):
	return [ord(c) for c in s]

# array of bytes
buffer = []

# header
buffer += str2ba("MThd")     # chunk ID
buffer += int2ba(6)          # chunk size
buffer += short2ba(0)        # format type
buffer += short2ba(1)        # number of tracks
buffer += short2ba(0x01E0)   # time division


# track 1 (the only track)
trackbuffer = []


buffer += str2ba("MTrk")         # track ID
buffer += int2ba(len(trackbuffer)) # chunk size
buffer += trackbuffer

midifile = open("out.midi", "w")
midifile.write("".join([chr(b) for b in buffer]))
midifile.close()


