from time import sleep

def count(x):
	while (x <= 1000):
		print(x, end = '\r')
		sleep(0.01)
		x+=1

count(0)
print ("║║╔║║╔╗ ║")
print ("╠╣╠║║║║ ║")
print ("║║╚╚╚╚╝ O")
