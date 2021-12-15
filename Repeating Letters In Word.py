# _____All Repeating Letters In Word______
name = input("Enter a Word: ")
dummy=[]
b=set(dummy)
for i in range(len(name)):
    j = i + 1
    while j < len(name):
        if name[i] == name[j]:
            b.add(name[i])
            j +=1
        else:
            j += 1
print("The repeating letters is/are: ",end='')
for i in b:
    print(i,end=" ")