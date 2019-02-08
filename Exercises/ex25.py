def break_words(stuff): # splits up a single string into multiple, with the split.(argument) acting as what determines individual 
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words): # takes a string/list/(tuple) and organises it alphabetically 
    """Sorts the words."""
    return sorted(words)

def print_first_word(words): # prints the word at location 0 and removes it from the list
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words): # prints the word at location -1 and removes it from the list
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence): # calls other functions before returning their values
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    return words

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print(words)
    print_first_word(words)
    print(words)
    print_last_word(words)
    print(words)
    return words
    