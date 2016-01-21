from music21 import *
from pprint import pprint

# https://www.youtube.com/watch?v=PSNPpssruFY

s = converter.parse('musicXML/aint_misbehavin.xml')

pprint(vars(s))

print(dir(note))