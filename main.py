from lib.musicStructures import *

n1 = Note( {"onset":0, "duration": 2, "pitch": 60})
n2 = Note( {"onset":1, "duration": 2, "pitch": 61})
n3 = Note( {"onset":2, "duration": 3, "pitch": 60})

n4 = Note( {"onset":0, "duration": 2, "pitch": 63})
n5 = Note( {"onset":1.2, "duration": 4, "pitch": 61})
n6 = Note( {"onset":2.1, "duration": 3, "pitch": 60})
n7 = Note( {"onset":3, "duration": -1})

f1 = Figure([n1, n2, n3])
f2 = Figure([n4, n5, n6, n7])

comparator = Comparator([f1, f2])