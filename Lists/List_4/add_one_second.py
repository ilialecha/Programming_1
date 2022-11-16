import sys

h, m, s = [ int(i) for i in sys.stdin.readline().split()]

if (0<=h<24) and (0<=m<60) and (0<=s<60):

	totalTime = (h*3600) + (m*60) + s +1

	newHour =  00 if  (totalTime // 3600) == 24 else "{:02d}".format(totalTime // 3600)
	newMin =  "{:02d}".format(totalTime % 3600 // 60)
	newSec =  "{:02d}".format(totalTime % 3600 % 60)

print(str(newHour)+":"+str(newMin)+":"+str(newSec))




