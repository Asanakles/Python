import sys
alph = 'abcdefghigklmnopqrstuvwxyz'
print 'Please write text and kay:'
text = sys.argv[1].lower()
shift = int(sys.argv[2])

'''
coded_text = ''
new_letter = ''
leter_position = None
for letter in text:
	leter_position = alph.find(letter)
	if leter_position != -1:
		new_letter = alph[(leter_position+shift)%len(alph)]
	else:
		new_letter = letter
	coded_text+=new_letter
print coded_text
'''
print shift