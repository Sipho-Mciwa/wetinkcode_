import re
import string

def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    text = list(filter(lambda word: word not in delimiters, text))              #filtering out all the delimiters
    list_ = "".join(text)
    words = list_.split()
    return(words)


def convert_to_word_list(text):
    delimiters = getDelimiters(text)
    list = split(delimiters, text)
    word_list = [word.lower() for word in list]
    return(word_list)


def words_longer_than(length, text):
    words = convert_to_word_list(text)
    new_Words = list(filter(lambda word: len(word) > length, words))
    return(new_Words)


def words_lengths_map(text):
    words = convert_to_word_list(text)
    length_list = list(map(lambda word: len(word), words))
    word_lengths = {key:0 for (key) in length_list }
    length_list.sort()
    for key in length_list:
        if key in word_lengths:
            word_lengths[key] += 1
    return(word_lengths)


def letters_count_map(text):
    alphabets = get_alphabet_characters()
    alphas_in_text = remove_Punctuations(text)
    letter_counter = {key:0 for (key) in alphabets}
    for key in alphas_in_text:
        if key in letter_counter:
            letter_counter[key] += 1
    return(letter_counter)
    

def most_used_character(text):

    if (text == ""):
        return (None)
    elif(len(text) > 0 and text != ""):
        
        letter_count = letters_count_map(text)
        items = list(letter_count.items())
        (Max, index) = getMax(letter_count)
        most_used = items[index]
        return(most_used[0][0])
        
def get_alphabet_characters():
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']
    return (alphabets) 
    
        
def getDelimiters(text):
    """
    This function gets a list of all the punctuation 
    marks and returns them as a joint string
    """
    set_del = {word for word in text if word in string.punctuation}          #I made this into a set to remove duplicates
    delimiters = list(set_del)
    return("".join(delimiters))


def getLowerChars(my_list):
    new_set = list(map(lambda letter: letter.lower(), my_list))
    return (new_set)


def remove_Punctuations(text):
    delimiters = getDelimiters(text)
    delimiters = delimiters[:] + ' '
    alphas = list(filter(lambda letter: letter not in delimiters, text))
    letters = (getLowerChars(alphas))
    letters.sort()
    return (letters)


def getMax(letter_count):
    occurences = [letter_count[key] for key in letter_count]
    Max = 0
    i = 0
    for item in occurences:
        if Max < item:
            Max = item
    i = occurences.index(Max)
    return(Max, i)
