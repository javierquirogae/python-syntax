




def print_upper_words(words, must_start_with):
    '''
    this will print each string that starts with the indicated chars in the list in all caps
    
    '''
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())



print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], ["h", "y"])