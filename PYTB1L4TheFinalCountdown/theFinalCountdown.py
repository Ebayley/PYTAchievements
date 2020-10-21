from time import sleep

def count(x):
	while (x >= 0):
		print(x, end = '\r')
		sleep(0.01)
		x-=1

count(1000)
print ("║║╔║║╔╗ ║")
print ("╠╣╠║║║║ ║")
print ("║║╚╚╚╚╝ O")
