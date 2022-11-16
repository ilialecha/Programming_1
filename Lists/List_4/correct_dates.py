import sys
def leapyear(y):
	return (y%4 == 0 ) and (y%100 != 0 or y%400==0)	

def correct_date(d, m, y):
	if m in [1,3,5,7,8,10,12] and 1<=d<=31: # Tienen 31 dias 
		return True
	elif m in [4,6,9,11] and 1<=d<=30: #Tienen 30 dias 
		return True 
	elif m==2 and (1<=d<=28 or leapyear(y) and 1<=d<=29) :
		return True
	else: 
		return False

line = sys.stdin.readline() #Obtain Data
while line!='':

    if correct_date(int(line.split()[0]), int(line.split()[1]), int(line.split()[2])):
        print("Correct Date")
    else:
        print("Incorrect Date")

    line = sys.stdin.readline()

    
	