first_name= input("Enter your first name:")
last_name= input("Enter your Last name:")

short_name= (first_name[0]+ "." +last_name[0:4])
#if the last name consists of less than four letter all wil be printed
print("Short name:", short_name)