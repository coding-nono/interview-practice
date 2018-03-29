

# Given a string, count number of words in it. 
# The words are separated by following characters: space ('') or new line ('\n') or tab ('\t') or a combination of these.
#

def count_words(input_string):
    i = 0 
    count_words = 0
    while i < len(input_string):
        if input_string[i] in ['\t', '\n', ' ']:
            while i < len(input_string)  and input_string[i] in ['\t', '\n', ' ']:
                i += 1
        else:
            count_words += 1
            while i < len(input_string) and input_string[i] not in ['\t', '\n', ' ']:
                i += 1

    return count_words


if __name__ == '__main__':

    assert count_words("An example of a \n \t string ") == 5
    assert count_words(" An example \t of a \n \t string") == 5
    assert count_words("asdasdsadasdasdas") == 1
    assert count_words("     ") == 0
    assert count_words("One two         three\n  four\tfive  ") == 5
