import os

def addtask(comm):
	file = open('tasklist.txt','a')
	if(os.stat("tasklist.txt").st_size != 0):
		file.write('\n')
	for c in comm[1:]:
		file.write(c+' ')
	file.close()
	return

def printtasks():
	file = open('tasklist.txt','r')
	op = file.readlines()
	for o in op:
		print(o,end='')
	file.close()
	return


stop = False
ip = input()
command = ip.split()


while(stop == False):
	if(command[0] == 'add'):
		addtask(command)
	ip = input()
	command = ip.split()
	if(ip=='exit'):
		stop = True
		printtasks()