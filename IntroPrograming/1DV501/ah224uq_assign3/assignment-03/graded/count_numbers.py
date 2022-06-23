def count_different(lst):
    list_set = set(lst)
    different = len(list_set)
    return different


def count_occurrences(lst):
    occurences = {}
    for element in lst:
        if element in occurences:
            num = occurences[element] + 1
            occurences[element] = num
        else:
            occurences[element] = 1

    return occurences


def get_key(dic, max_value):
    for k, v in dic.items():
        if max_value == v:
            return k


def read_and_process(location, delimeter):
    with open(location, 'r') as file:
        lst = []
        for line in file:
            line = line.strip().split(delimeter)
            row_list = [lst.append(int(x)) for x in line]

        return lst


def result():
    try:
        file1 = 'assignment-03/graded/file_10000integers_A.txt'
        lst = read_and_process(file1, ', ')
        different = count_different(lst)
        print()
        print("Number of different integers in text file 1 are:", different)

        occurences = count_occurrences(lst)
        #  print("\nNumber and their count are: ")
        #  print(occurences)
        # print(3 * "\n")

        max = 0
        for number in occurences.values():
            if number > max:
                max = number

        print('The most frequent number is :', get_key(occurences, max))

        print()
    except FileNotFoundError:
        print('File does not exist')

    try:

        file2 = 'assignment-03/graded/file_10000integers_B.txt'

        lst = read_and_process(file2, ':')
        different = count_different(lst)
        print("\nNumber of different integers in text file 2 are:", different)
        occurences = count_occurrences(lst)
        # print("Number and their count are: ")
        # print(occurences)

        max = 0
        for number in occurences.values():
            if number > max:
                max = number

        print('The most frequent number is :', get_key(occurences, max))

    except FileNotFoundError:
        print('File does not exist')


result()

