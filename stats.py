def word_count ( book_string ):
    words = book_string.split()
    return len (words)

def character_count ( book_string ):
    book = book_string.lower ()
    #Dictionary to store letter counts
    characters = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }

    for entries in characters:
        for letter in book:
            if entries == letter:
                characters [entries] += 1
    return characters

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]

#takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
def sort_characters ( unsorted ):
    sorted = []
    for entry in unsorted:
       sorted.append( {"char": entry, "num": unsorted [entry]} )
    sorted.sort (reverse = True, key = sort_on)
    return sorted
    