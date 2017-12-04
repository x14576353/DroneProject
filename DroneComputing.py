import dweepy

def importUserData():



def getPhotoPoint():


def getObjectAmm():

def get_file():
	with open ('thingName.txt','r') as text:
		for sen in text:
			return sen.strip('\')
			
def post (signal):
	thing = get_file()
	print dweepy.dweet_for(thing,signal)
	

	
while True:
	Utime = importUserData();
	signal = getObjectAmm();
	post(signal)
	time.sleep(Utime)