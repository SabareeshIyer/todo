import os

def addTask(comm):
	file = open('tasklist.txt','a')
	if(os.stat("tasklist.txt").st_size != 0):
		file.write('\n')
	for c in comm[1:]:
		file.write(c+' ')
	file.close()
	return

'''def printtasks():
	file = open('tasklist.txt','r')
	op = file.readlines()
	for o in op:
		print(o,end='')
	file.close()
	return
'''

def showTasks():
	file = open('tasklist.txt','r')
	i = 1
	op = file.readlines()
	for o in op:
		print(i,o,end='')
		i = i+1
	file.close()
	return

def deleteTasks(linenum):
	file = open('tasklist.txt','r+')
	d = file.readlines()
	numb = int(linenum)
	file.seek(0)
	count = 1
	for i in d:
		if(count != numb):
			file.write(i)
		count = count +1
	file.truncate()
	file.close()
	return

def editTask(linenum, desc):
	file = open('tasklist.txt','r+')
	d = file.readlines()
	numb = int(linenum)
	file.seek(0)
	count = 1
	for i in d:
		if(count != numb):
			file.write(i)
		if(count == numb):
			file.write(desc+'\n')
		count = count +1
	file.truncate()
	file.close()
	return


def bulkDelete():
	return

def man():
	print('Command(s)	:		Description\n'+
			'add 		:		Add new task\n'+
			'del, delete	:		Delete task\n'+
			'bdel 		:		Bulk delete\n'+
			'show 		:		Show task list\n'+
			'edit 		:		Edit task\n')
	return

stop = False
ip = input()
command = ip.split()


while(stop == False):
	case = command[0]
	if(case == 'add'):
		addTask(command)
	elif(case == 'show'):
		showTasks()
	elif(case == 'del' or case == 'delete'):
		deleteTasks(command[1])
	elif(case == 'edit'):
		editTask(command[1],command[2])
	elif(case == 'man'):
		man()

	ip = input()
	command = ip.split()
	if(ip=='exit'):
		stop = True
		#printtasks()