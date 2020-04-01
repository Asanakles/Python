import sys

key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
text = []

for now in sys.argv:
	text.append(now)
del text[0]

result = []
for x in text:
	x=x.replace(' ','').replace("'",'').replace('"','').replace('[','').replace(']','')
	result+= x

result = result[:len(result)//5*5]

i=0
answer = ''
while i<len(result):
	if result[i].isupper():
		result[i] = 'b'
	else:
		result[i] = 'a'
	if (i+1)%5==0:
		text_now = ''
		for y in range(5):
			text_now+= result[y+i-5+1]
		answer+= alphabet[key.find(text_now)]
	i+=1
print answer