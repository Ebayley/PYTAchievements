sentence = input("Please write down a sentence:\n")
stutter = sentence.split()
for x in stutter:
	if len(x) > 2:
		print(x[0:2] + ".. " + x[0:2] + ".. " + x + " ", end=" ")
	else:
		print(x, end=" ")