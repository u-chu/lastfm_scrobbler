#!/usr/bin/env python

import os
import time
import pylast
from  mutagen.id3 import ID3
from  mutagen.mp3 import EasyMP3 as MP3
import hashlib
import sys

#print allfiles
#exts=[]
network = pylast.LastFMNetwork(
			api_key='06e2c700f0b1403ccc5752a711319a68', 
			api_secret='2807db680518fbe208d6edb8b2681500',
			username='', #<---------------------------your login
			password_hash=hashlib.md5("").hexdigest()#<--------------your password  plain-text
			#password_hash='' #<-------------if you know md5 hash of your password, you may put it into this line, uncomment it, and comment previous line
			) 
#for i in exts:
if len(sys.argv)>1:
	files=sys.argv
else: files=os.listdir('.')
#print files
#files=files.sort(key=lambda x: os.path.abspath(x))
files=filter(lambda x: x.endswith(('.MP3','.mp3')), files)
	#print i
	#print files
if files == []:
	print "Nothing found!"
	exit()
files.sort()
#print files
i=1
for f in files:
	ids=ID3(f)
	#~ print ids
	try:
		artist=ids['TPE1']
	except:
		try:
			artist=ids['TPE2']
		except:
			artist=''
	try:
		album=ids['TALB']
	except:
		album=''
	try:
		title=ids['TIT2']
	except:
		title=''
	#~ print ids
	print('%i %s / %s / %s'%(i, artist, album, title))
	#lastfm_user = network.get_user(self.username)
	res=network.scrobble(artist=artist, title=title, timestamp=int(time.time()))
	#print res
	i=i+1
	time.sleep(3)

