number=int(input())
steps=0
while number>1:
    if number%2==0:
        number=number//2
        steps+=1
        print(number)
    else:
        number=number*3+1
        steps+=1
        print(number)
print("steps=",steps)    
