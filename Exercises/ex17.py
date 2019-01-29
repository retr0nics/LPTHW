from sys import argv
from os.path import exists #importing the exists module from os.path library

script, file_A, file_B = argv # unpacking argv # pylint: disable=unbalanced-tuple-unpacking

#print(f"You have launched {script} Copying from {file_A} to {file_B}")

# we could do these two on one line, how?  (lies)
object_A = open(file_A).read() # creating file object
#data_A = object_A.read() # call read on our open file object and store data in variable

#print(f"The input file is {len(data_A)} bytes long and contains {data_A} information") # inside fstring, call len function and pass our from file as argumment

#print(f"Does the output file exist? {exists(file_B)}") # inside the fstring, call exists function and pass our target file as argument
#print("Ready, hit RETURN to continue, CTRL-C to abort.")
#input()

object_B = open(file_B, 'w').write(object_A) #opens file object and stores it in var, created if not exists already
#object_B.write(object_A) # writes the contents of data_A

#print("Alright, all done.")
#print("Press any key to save the file")
#input("...")

#object_B.close() #saves the file
#object_A.close() #saves the file