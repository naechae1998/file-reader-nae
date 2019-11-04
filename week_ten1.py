import os #Still not Quite sure what an OS library is but getting a good grip on using the import function
filep =input("please enter directory to store file ")
filePath = filep
fN= input ("filename: ");
completePath = filePath+fN
if os.path.isfile(fN): # file exists?
 print('File Exists')
else:
  open(fN, "w+")
if os.path.isdir(filePath): # file path exists?
 print('The directory is Valid')
if os.path.exists(completePath): #complete path exist?
 print(' It is a complete path!')
print('Your Complete Path is: ',completePath)
with open(fN, 'w+') as fileHandle: #open file for writing
 n=input("please Enter address Name and Phone Number: ")
print(" The name of your new file is " + fN + "!")
print (n) #Just reprinted what was entered since fN.readlines() isnt working
#print (fN.readlines()) #this is supposed to show what is inside the file I keep getting errors like theAttributeError: 'str' object has no attribute

