import statistics


def mean(lst):
    average = sum(lst) / len(lst)
    return average


def std(lst):
    # new_list = [x * x for x in lst]
    # standard_deviation = sum(new_list) / len(new_list)
    # standard_deviation = math.sqrt(standard_deviation)
    standard_deviation = statistics.stdev(lst)
    return standard_deviation


def read_and_process():
    try:
        with open('assignment-03/graded/file_10000integers_A.txt', 'r') as file:
            lst_1 = []
            for line in file:
                line = line.strip().split(', ')
                [lst_1.append(int(x)) for x in line]

            print("Mean and Standard deviation of file A \n")

            print("Mean is : %.4f" % mean(lst_1))
            print("Standard Deviation : %.4f" % std(lst_1))


    except FileNotFoundError:
        print('File does not exist')

    try:

        with open('assignment-03/graded/file_10000integers_B.txt', 'r') as file:
            lst_2 = []
            for line in file:
                line = line.strip().split(':')
                row_list = [lst_2.append(int(x)) for x in line]

            print("\nMean and Standard deviation of file B  \n")

            print("Mean is :  %.4f" % mean(lst_2))
            print("Standard Deviation : %.4f" % std(lst_2))


    except FileNotFoundError:
        print('File does not exist')


read_and_process()
