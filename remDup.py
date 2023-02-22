my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
res=[]
for i in my_list:
    if i not in res:
        res.append(i)
my_list=res
print("The list with unique elements only:")
print(my_list)
