import os
from os.path import isfile, join

def getFileList(path):
	list = []
	for f in os.listdir(path):
		if isfile(join(path,f)):
			list.append(f[:f.index('.')])
		else:
			list.append(getFileList(join(path,f)))
	return list

def makeOutput(songList):
	sl = ['\n'.join(sorted(s)) for s in songList]
	sl = '\n\n'.join(sl)
	return sl

def writeOut(path,list):
	file = open(path,"w")
	for song in list:
		file.write(song)

readPath = "/path/to/dir"
writePath = readPath+"/songList.txt"

try:
	os.remove(writePath)
except:
	pass

output = makeOutput(getFileList(readPath))
writeOut(writePath, output)
