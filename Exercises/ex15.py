from sys import argv # imports argv module

script, filename = argv # unpacks contents of argv

txt = open(filename) # opens the file as a file object

print(f"Here's your file {filename}:") # prints my filename
print(txt.read()) # calls the read function on the file object

txt.close