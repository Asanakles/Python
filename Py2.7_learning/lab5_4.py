import sys

way = []
def file_search(folder, filename):
	if filename == folder:
		way.append(filename)
		return '/'.join(way)
	elif type(folder) != list or len(folder) <= 1:
		if way!=[]:
			way.pop()
			return False
	else:
		for x in folder:
			way.append(folder[0])
			if file_search(x,filename):
				return '/'.join(way)
	return False	
'''
print file_search([ 'D:', 
	['recycle bin'], 
	['tmp', 
	['old'], 
	['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak' ] ], 'hey.py'], 'find.me')

print file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt')
way = []
print file_search([ '/home', 
	['user1'], 
	['user2', 
	['my pictures'], 
	['desktop', 'not this', 'and not this', 
	['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z',
	 ['user3', 
	 ['temp'], ], 'hey.py'], 'hereiam.py')
'''
#print file_search(['C:'], 'crack.exe')
print file_search(['C:', '1.txt', '2.txt', '3.txt', '4.txt'], '4.txt') 