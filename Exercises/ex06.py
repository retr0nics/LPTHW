#assigns variables
types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# assigned a format string into a variable
y = f"Those who know {binary} and those who {do_not}."

# prints the variables
print(x)
print(y)

# prints format strings
print(f"I said: {x}")
print(f"I also said: '{y}'")

#assigns a variable a boolean value
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
#evokes the joke evaluation variable with added format parameter
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

#prints the addition of 2 variables
print(w + e)
