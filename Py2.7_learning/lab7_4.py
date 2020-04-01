import sys
import datetime

x_time = datetime.datetime.today()
that_t = ''

def create_calendar_page(my_month = x_time.month, my_year = x_time.year):
	that_t = x_time.replace(year = my_year, month = my_month)
	days = [31,28,31,30,31,30,31,31,30,31,30,31]
	if that_t.year%4 ==0:
		days[1] = 29
	rezult = '--------------------\nMO TU WE TH FR SA SU\n--------------------\n'
	my_weeks = ''
	for j in range(that_t.replace(day=1).weekday()):
		my_weeks+='   '	
	
	for i in range(days[that_t.month-1]):
		if that_t.replace(day=i+1).weekday()==6:
			if i+1<10:
				my_weeks+='0' + str(i+1)
			else:
				my_weeks+=str(i+1)
			rezult+=my_weeks+'\n'
			my_weeks = ''
		else:
			if i+1<10:
				my_weeks+= '0' + str(i+1) + ' '
			else:
				my_weeks+= str(i+1) + ' '
	if that_t.replace(day=days[that_t.month-1]).weekday()!=6:
		rezult+=my_weeks[0:-1]
		return rezult
	rezult = rezult[:-1]
	return rezult

print create_calendar_page()