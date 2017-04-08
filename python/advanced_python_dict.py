import csv

with open('metis/prework/dsp/python/faculty.csv') as readfile:
	reader = csv.reader(readfile)

	def first_question():
		mydict = {}
		value = []

		for rows in reader:

			key = rows[0].split()[-1]
			values = rows[1:4]
			
			removal = values[1].replace('Biostatistics','')
			values[1]=removal

			split = values[1].split()
			new = ''

			for x in split:
				if len(x)<4:
					split.remove(x)
					new = ' '.join(split)
					values[1] = new

				else:
					new = ' '.join(split)
					values[1] = new

			if key in mydict:
				value.append(values)
			else: 
				value = [values]

			mydict[key]=value

		first_three = {k: mydict[k] for k in mydict.keys()[:3]}
		print(first_three)

	def second_question():

		mydict = {}
		value = []

		for rows in reader:

			key = (rows[0].split()[0], rows[0].split()[-1])
			values = rows[1:4]
			
			removal = values[1].replace('Biostatistics','')
			values[1]=removal

			split = values[1].split()
			new = ''

			for x in split:
				if len(x)<4:
					split.remove(x)
					new = ' '.join(split)
					values[1] = new

				else:
					new = ' '.join(split)
					values[1] = new

			if key in mydict:
				value.append(values)
			else: 
				value = [values]

			mydict[key]=value

		first_three = {k: mydict[k] for k in mydict.keys()[:3]}
		#print(first_three)
		return mydict


	def third_question():

		mydict = second_question()
		sorted_keys = sorted(mydict, key = lambda x: x[1])

		for key in sorted_keys:
			print(str(key) + str(mydict[key]))

	third_question()












