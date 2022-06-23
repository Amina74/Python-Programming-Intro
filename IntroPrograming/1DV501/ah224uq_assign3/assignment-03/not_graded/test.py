import os
path = os.getcwd()
print("Current dir:", path)

subdir = os.chdir('ah224uq_assign1')
print()
print("Moved to dir:", os.getcwd())
print()
print(subdir)