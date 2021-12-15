# _________Most Repeated Letter In a Word________
name = input("Enter a Word: ")
count = 2
dummy = []
ans = set(dummy)
for i in range(len(name)):
    countn = name.count(name[i])
    if countn == 1:
        continue
    elif countn > 1 and countn == count:
        ans.add(name[i])
    elif countn > count:
        ans.clear()
        ans.add(name[i])
        count += 1
print("The most repeated characters is/are: ",end="")
for i in ans:
    print(i,end=" ")