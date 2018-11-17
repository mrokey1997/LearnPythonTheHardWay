from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print(f"Copying from {from_file} to {to_file}")
print("Moving from {from_file} to {to_file}")

# we could do these two on one line, how?

in_file = open(from_file, 'r+') # read and write but can't erase??
indata = in_file.read()

in_file.truncate()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exists? {exists(to_file)}")
print("Ready, hit RETURN to countinue, else CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done")

out_file.close()
in_file.close()