# user_input = input("what's on your mind today? - ")
# words = user_input.split(" ")
# print(f"oh nice, you just told me what's on your mind in {len(words)} words!")

acronym_dict = {'As Soon As Possible': 'ASAP', 'World Health Organization': 'WHO', 'Absent Without Leave': 'AWOL'}


def check_acronym(acronym):
    if acronym in acronym_dict:
        return acronym_dict[acronym].upper()
    else:
        print('Acronym found found in our records ...')


u_input = input('Enter the text to check acronym for : ')
print(check_acronym(u_input.strip()))