

def lexicographic_permutation(input_string):
    i = 0
    first = None
    while i < len(input_string) -1:
        if input_string[i] < input_string[i+1]:
            first = i
        i += 1
    
    if not first:
        raise Exception("No more permutation")
    j = 0
    to_rep =0
    while j < len(input_string):
        if input_string[j] > input_string[first]:
            to_rep = j
        j += 1 
    input_string = list(input_string)
    input_string[first], input_string[to_rep] = input_string[to_rep], input_string[first]
    input_string = input_string[:first+1] + input_string[first+1:][::-1]
    res = "".join(input_string)
    return "".join(input_string)

if __name__ == '__main__':
    assert lexicographic_permutation('abcd') == 'abdc'
    assert lexicographic_permutation('abdc') == 'acbd'
