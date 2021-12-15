# _____To find the first repeating letter in a word______
name = input("Enter a Word: ")
for i in range(len(name)):
    j = i + 1
    while j < len(name):
        if name[i] == name[j]:
            print("The first repeating character is:", name[i])
            exit(0)
        else:
            j += 1
print("No repeating letter in the word!!")
