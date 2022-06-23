import statistics


def median(lst):
    return statistics.median(lst)


def avrage(lst):
    return statistics.mean(lst)


def gab(lst):
    diff = max(lst) - min(lst)
    return diff


# Read multiple space separated integers from keyboard
text = input("Provide salarties: ")
words = text.split()
ints = [int(w) for w in words]
print("The meandean is", median(ints), "\nThe mean is", avrage(ints),
      "\nThe gap is", gab(ints))
# main
# mylist = [21700, 28200 ,26300,  25100, 22600, 22800, 19900 ]
