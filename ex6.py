types_of_people = 10
x = f"There are {types_of_people} types of people."
types_of_people = types_of_people * 2


binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x) # There are 10 types of people.
x = x
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = "No"
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)