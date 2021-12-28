
relno=0
with open('relversion') as frel:
	rel = frel.readline()
	relno = int(rel)
	relno += 1
	relv = "0.%d" % relno

print("Release branch ",relv)
