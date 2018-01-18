	import random  
	  
	f = input("Enter file name without extension:")  
	fin = f+".txt"  
	fout = f + "Scrambled.txt"  
	  
	try:  
	  fileRead = open(fin,"r")  
	  fileWrite = open(fout,"w")  
	except FileNotFoundError:  
	  print("File does not exist , So a file with same name will be created by the system")  
	  Enteredtext = input("Enter text to save into the new file:")  
	  fileNew = open(fin,"w")  
	  print(Enteredtext, file = fileNew)  
	  fileNew.close()   
	     
	  fileRead = open(fin,"r")  
	  fileWrite = open(fout,"w")   
	    
	def ReOrder(Currentword):  #Function to re order the word   
	    final = ""             
	    if(len(Currentword) <= 3):  
	         return Currentword  
	      
	    firstChar = Currentword[0]  
	    lastChar = Currentword[-1]  
	    middleChar = Currentword[1:-1]  
	      
	    if(lastChar == "." or lastChar == "?" or lastChar == "!" or lastChar == "," or lastChar == ";" ):  
	        lastChar = Currentword[-2:]  
	        middleChar = Currentword[1:-2]  
	          
	    if(len(middleChar) == 1):  
	        return middleChar  
	    else:  
	        middleChar = list(middleChar)  
	        random.shuffle(middleChar)  
	        newWord =''.join(middleChar)  
	      
	    return firstChar+newWord+lastChar  
	         
	    
	for readLine in fileRead:  
	   readLine = readLine.strip()  
	   NewLine = ""  
	      
	   for word in readLine.split():  
	        NewLine+=ReOrder(word)+" "  
	      
	   print(NewLine,file = fileWrite)   
