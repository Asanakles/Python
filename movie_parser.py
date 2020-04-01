import re

file_movie = open('test.txt','r')
movies = []
i = 0
for x in file_movie:
	while x[-1]=='\t' or x[-1]=='\n':
		x = x[:-1]
	movies.append(x.split('[\\/_O_o_\\/]'))
	for y in range( len(movies[i]) ):

		#found date (year)	
		if re.search('\(\d{4}\)', movies[i][y]) !=None:
			temp = movies[i][y].index(str( re.search('\(\d{4}\)',movies[i][y]).group() ))
			movies[i].append(movies[i][y][temp:temp+6])
			movies[i][y] = movies[i][y][:temp]	

		#delete empty places
		if movies[i][y][0]==' ' or movies[i][y][-1]==' ':
			while movies[i][y][0]==' ' or movies[i][y][-1]==' ':
				if movies[i][y][0]==' ':
					movies[i][y] = movies[i][y][1:]
				elif movies[i][y][-1]==' ':
					movies[i][y] = movies[i][y][:-1]

	#added empty plase if that movie dont have translate name
	if len(movies[i])==2:
			movies[i].insert(1, '') # '!!!no translate!!!')
			movies[i].insert(2, '') # '!!!no translate!!!')
	elif len(movies[i])==3:
		movies[i].insert(1, '') # '!!!no translate!!!')

			
	#tested correct lenght
	if len(movies[i])!=4:
		print (movies[i])

	#tested correct date parse
	if movies[i][-1][-1]!=')':
		print (movies[i])
		

	i+=1

#print ()
#print (str(movies[5]) + 'END')



file_movie.close()
rez_file = open('rezult.txt','w')

for line in movies:
	for arguments in line:
		rez_file.write(str(arguments) + ' ')
	rez_file.write('\n')

rez_file.close()

rez_0 = open('rez_0.txt','w')
rez_1 = open('rez_1.txt','w')
rez_2 = open('rez_2.txt','w')
rez_3 = open('rez_3.txt','w')

for line in movies:
	rez_0.write(str(line[0]) + "\n")
	rez_1.write(str(line[1]) + "\n")
	rez_2.write(str(line[2]) + "\n")
	rez_3.write(str(line[3]) + "\n")


rez_0.close()
rez_1.close()
rez_2.close()
rez_3.close()