#Rendi Noober
import os, sys, time

def start():
	start=input('enter to start')
	if start=="" or start==" ":
		os.system("")
	else:
		print("please enter to start!!")
	
while True:
	#try
	try:
		startTime=time.time()
		print("start")
		while True:
			second=round(time.time() - startTime,3)
			print("second:",second)
		
	# stoped
	except KeyboardInterrupt:
		print("\nStoped")
		endTime=time.time()
		print("total time:", endTime - startTime, 3),"second"