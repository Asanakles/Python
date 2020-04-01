import sys

morse_code = {
    "A" : ".-", 
    "B" : "-...", 
    "C" : "-.-.", 
    "D" : "-..", 
    "E" : ".", 
    "F" : "..-.", 
    "G" : "--.", 
    "H" : "....", 
    "I" : "..", 
    "J" : ".---", 
    "K" : "-.-", 
    "L" : ".-..", 
    "M" : "--", 
    "N" : "-.", 
    "O" : "---", 
    "P" : ".--.", 
    "Q" : "--.-", 
    "R" : ".-.", 
    "S" : "...", 
    "T" : "-", 
    "U" : "..-", 
    "V" : "...-", 
    "W" : ".--", 
    "X" : "-..-", 
    "Y" : "-.--", 
    "Z" : "--.."
}

def retrance(signal):
	rez_signal = ''
	for x in signal:
		if x =='.':
			rez_signal+='^_'
		elif x=='-':
			rez_signal+='^^^_'
	rez_signal = rez_signal[:-1]
	return rez_signal

def encode_morze(text):
	text = text.upper()
	rez_code = ''
	for x in text:
		if x==' ':
			rez_code+='____'
		elif x.isalpha():
			rez_code+= retrance(str(morse_code.get(x)))+'___'
	rez_code = rez_code[:-3]
	return rez_code

print encode_morze('HOUSTON WE HAVE A PROBLEM')
