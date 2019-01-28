from sys import argv # import from sys the argv module

script, filename = argv # unpacks  argv contents and stores

print(f"We're going to erase {filename}.")
print("If you dont want that, press CTRL + C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w') # opens the file in write mode

print("Truncating the file. Goodbye!")
target.truncate() # empties the file contents

print("Now I'm going to ask you for three lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
# adds the user inputs to the file object

print("Lets commit those changes...please confirm.")
input("?")
target.close() # closes (saves) the file

print("The file now contains:\n")
target = open(filename) #opens the file in read (defaulted)
print(target.read()) # reads the file obj and prints

input("Press any key to close the program.")
target.close()
