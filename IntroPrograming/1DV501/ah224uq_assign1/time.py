time = int(input("Give a number of seconds: "))
hours = (time / 3600)
minutes = (time / 60) % 60
seconds = (time % 60)
print("This coressponds to :", int(hours), "hours", int(minutes), "minutes", "and ", int(seconds), "seconds.")
