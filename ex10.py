tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat
)
print("I'm") # Output: I'm
print('I"m') # Output: I"m

print("ASCII bell: \ahmm"
	+ "\nASCII backspace: \bhmm"
	+ "\nASCII formfeed: \fhmm"
	# + "\nCharacter named name in the Unicode database (Unicode only): \N{baron}hmm")
	+ "\nCharacter with 16-bit hex value xxxx: \uAAAA"
	# + "\nCharacter with 32-bit hex value xxxxxxxx: \UAAAAAAAA"
	)