dict1={}
dict2={}
n1=int(input("total no: of elements in the dict1 :"))
n2=int(input("total no: of elements in the dict2:"))
for i in range(n1):
    dict1[i]=int(input("Enter the element in dict1:"))
for i in range(n2):
    dict2[i]=int(input("Enter the element in dict2:"))
print("elements in dict1:",dict1)
print("elements in dict2:",dict2)
dict1.update(dict2)
print("Merged elements :",dict1)
