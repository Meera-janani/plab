test_string = input("enter the string: ")
total = 1

for i in range(len(test_string)):
   if(test_string[i] == ' ' or test_string == '\n' or test_string == '\t'):
      total = total + 1

print("Total Number of Words in our input string is: ", total)
