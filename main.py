#converts a book in a text file into a string
from stats import word_count
from stats import character_count
from stats import sort_characters
import sys

def get_book_text ( path ):
    with open (path) as book:
        book_string = book.read()

    return book_string

#Coded using Frakenstein as a test.  Variable names are based off of frankenstein - not a generic book
def main ():
    if (len (sys.argv) != 2):
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_book = sys.argv [1]

    frank = get_book_text ( path_to_book )
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {path_to_book}")

    print ("----------- Word Count ----------")
    print (f" Found {word_count (frank)} total words")

    print ("--------- Character Count -------")
    letter_dictionary = sort_characters ( character_count ( frank ) )
    for i in range (0, len ( letter_dictionary ) ):
        print (f"{letter_dictionary[i]["char"]}: {letter_dictionary[i]["num"]}")
        
    print ("============= END ===============")


main ()