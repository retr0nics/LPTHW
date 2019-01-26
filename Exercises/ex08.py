lemons = "{} {} {} {}"

print(lemons.format(1, 2, 3, 4))
print(lemons.format("one", "two", "three", "four" ))
print(lemons.format(True, False, False, True))
print(lemons.format(lemons, lemons, lemons, lemons))
print(lemons.format(
    "Try your",
    "Own text here", 
    "Maybe a poem",
    "Or a song about fear"
))