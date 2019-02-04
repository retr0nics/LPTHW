from sys import argv #import modules

script, input_file = argv # unpack argv arguments to variables

def print_all(f): # define function that takes calls .read on the passed argument
    print(f.read())

def rewind(f): # defs function that takes calls .seek, putting the read to byte 0
    f.seek(0)

def print_a_line(line_count, f): # defs func that takes 2 arguments
    print(f"Line count is: {line_count}")
    print(line_count, f.readline()) # prints one argument and reads a single line on the other

current_file = open(input_file) # opens file object

print("First let's print the whole file:")

print_all(current_file) # calls the function with the current file object

print("Now let's rewind, kind of like a tape.")

rewind(current_file) # calls the function with the current file object, rewinding the file position

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

#rewind(current_file)

current_line += 1
print_a_line(current_line, current_file)
