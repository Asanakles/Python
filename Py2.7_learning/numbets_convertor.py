import sys

# convert numbers for 1-36 sistem to 1-36 sistem
def	convert_n_to_m(x,n,m):
	text = '0123456789abcdefghijklmnopqrstuvwxyz'
 	text = text.upper()
	basic = []
	for i in range(len(text)):
		basic.append(text[i])
	basic_n = basic[:n]
	basic_m = basic[:m]

	if type(x)!=int and type(x)!=str and type(x)!=long:
		return False
	
	elif type(x)==str:
		if not x.isalnum():
			return False
	elif type(x)==int:
		if x<0:
			return False

	if type(x)==long:
		x = str(x)
	
	x_tens = 0
	x_m = ''
	if type(x)==str:
		while x[0] =='0' and len(x)>1:
			x = x[1:]

	if type(x)==int:
		if x == 0:
			return 0
		temp = ''
		while x>0:
			temp=str(x%10) + temp
			x/=10
		x = temp
	x = list(x.upper())
	
	if basic.index(max(x))+1> n:
		return False

	#convertation N to 10 format
	for i in range(len(x)):
		x_tens+= len(basic_n)**(len(x)-i-1)*basic.index(x[i])
	#print 'x_tens='
	#print x_tens

	if x_tens ==0:
		return 0
	
	if m == 1:
		for i in range(x_tens):
			x_m += '0'
		return x_m

	#convertation X from 10 to M system
	while x_tens + m > m :
	#for i in range(len(str(x_tens))+1):
		#print x_m
		#if basic_m[x_tens%len(basic_m)]!='0':
		x_m = basic_m[x_tens%len(basic_m)] + x_m
		x_tens = x_tens/len(basic_m)
	while x_m[0] == '0' and len(x_m)>1:
		x_m = x_m[1:]
	return x_m
	


#print convert_n_to_m(123, 4, 1)
#print convert_n_to_m("A1Z", 36, 16)
print convert_n_to_m('bnh34521', 11, 14)
