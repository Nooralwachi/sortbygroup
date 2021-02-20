def groupbycol(filename):
	users={}
	result=[]
	with open (filename, 'r') as file:
		for line in file:
			line = line.strip()
			col = line.split()
			if col[1] not in users:
				users[col[1]] = [line]
			else:
				users[col[1]].append(line)
		#print(users)
	
	sorted_users= sorted(users.items(), key = lambda x:x[0])
	#print(sorted_users)

	
	for x,y in sorted_users:
		result.extend(y)
		lines= ('\n').join(result)
	#print(lines)

	with open('output.txt', 'w') as file:
		file.write(lines)




groupbycol("users.txt")
