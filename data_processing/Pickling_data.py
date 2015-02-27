""" Pickling data """

import pickle

from pattern.web import *
DC_Italian = URL('https://www.gutenberg.org/cache/epub/1012/pg1012.txt').download()
DC_English = URL('https://www.gutenberg.org/cache/epub/41537/pg41537.txt').download()
DC_German = URL('https://www.gutenberg.org/cache/epub/8085/pg8085.txt').download()

f = open('DC_Orig_Italian','w')
pickle.dump(DC_Italian,f)
f.close()

f = open('DC_Orig_English','w')
pickle.dump(DC_English,f)
f.close()

f = open('DC_Orig_German','w')
pickle.dump(DC_German,f)
f.close()