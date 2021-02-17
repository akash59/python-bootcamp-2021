from collections import Counter
import pdb

my_list = [2, 2, 2, 2, 4, 34, 325, 56, 78, 89, 3, 2, 3, 4, 5, 6, 7]
print(Counter(my_list))

my_string = 'hello my name is aakash sood'
my_string = my_string.replace(" ", "")
print(Counter(my_string))
counted_string = Counter(my_string)

print(counted_string.items())
print(counted_string.most_common(2))

dict_1 = dict(Counter(my_string))
print(dict_1)

my_string_1 = 'How many times do we appear in this line? How many ?'
d = dict(Counter(my_string_1.split(" ")))
print(d)


def count_occurrence(input_str):
    if len(input_str) <= 1:
        raise RuntimeError('Not a valid input. Please try again !!')
    input_str = input_str.lower().replace(" ", "")
    my_dict = {}
    for ch in input_str:
        if ch not in my_dict:
            my_dict[ch] = 1
        else:
            my_dict[ch] += 1
    return my_dict


pdb.set_trace()
char_occurrences = count_occurrence('Druva is my fourth company in my career !!')
print(char_occurrences)

char_occurrences = count_occurrence('D')
print(char_occurrences)
