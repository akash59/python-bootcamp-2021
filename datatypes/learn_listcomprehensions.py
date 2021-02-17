word = 'python'
my_list = [letter for letter in word]
print(my_list)

my_list = [letter*2 for letter in word]
print(my_list)

my_nums = [num for num in range(0, 11)]
print(my_nums)

my_nums = [num**2 for num in range(0, 11) if num % 2 == 0]
print(my_nums)

results = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
print(results)

my_list = []
for x in [10, 20, 30]:
    for y in [1, 2, 3]:
        my_list.append(x * y)
print(my_list)

my_list = [x * y for x in [10, 20, 30] for y in [100, 200, 300]]
print(my_list)

st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print('even!')

st = 'Create a list of the first letters of every word in this string'
print([word[0] for word in st.split()])