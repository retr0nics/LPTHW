people = 30 #assigns
cars = 40 #assigns
trucks = 35 #assigns

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks and cars > people:
    print("Thats too many vehicles.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still cant decide.")

if people > trucks:
    print("Alright, let's just take the trucks")
else:
    print("Fine, lets just stay home then!")