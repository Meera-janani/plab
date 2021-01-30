N=int(input("Enter total no of elements in a list:"))
lists=[]
for i in range(N):
    value=int(input("Enter the numbers in the list:"))
    lists.append(value)
    pos_value=(num for num in lists if num>=0)
    print("Positive Numbers in the list are:",*pos_value)
