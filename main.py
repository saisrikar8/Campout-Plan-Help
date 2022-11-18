#!/usr/bin/env python3
def getWeather():
	#From https://scoutlife.org/about-scouts/merit-badge-resources/programming/42476/python/
	 
	#...initialize looping variable, assume 'yes' as the first answer
	continueYN = 'y'
	 
	while continueYN == "y" or continueYN == "yes":
	   #...get temperature input from the user
	   sDegreeF = input("Enter next temperature in degrees Fahrenheit (F):")
	 
	   #...convert text entry to number value that can be used in equations
	   nDegreeF = int(sDegreeF)
	 
	   #...convert temperature from F to Celsius
	   nDegreeC = (nDegreeF - 32) * 5 / 9	
	 
	   print ("Temperature is about " +  str(round(nDegreeC, 3)) + " degrees Celsius")
	 
	   #...check for temperature below freezing..
	   if nDegreeC < 0:
	      print ("Pack long underwear!")
	 
	   #...check for it being a hot day...
	   if nDegreeF > 100:
	      print ("Remember to hydrate!")
	 
	   continueYN = (input("Input another temperature?:\n")).lower()
# --------Everything below this point is my code---------
def getPackingList():
	print("What do you plan on packing?", "\n\n")
	list = [];
	cont = "y"
	while cont == "y" or cont == "yes":
		item = input("Enter an item: ")
		list.insert(len(list) - 1,item)
		cont = input("Do you want to enter another item?: ")
	print("Here is your list:\n")
	for i in list:
		print(i)
	print("\n");
	#exit the program

print("Welcome!")
get = input("What would you like to do?:\nEnter 1 if you want to get advice based on weather\nEnter 2 if you want to create a packing list\n");
while get == "1" or get == "2":
	if (get == "1"):
		getWeather()
	elif(get == "2"):
		getPackingList()
	get = input("Would you like to continue?:\nEnter 1 if you want to get advice based on weather\nEnter 2 if you want to create a packing list\nEnter 'no' or 'n' if you don't want to do anything else\n")