vowels = "aeiouAEIOU"
list = []
ask = input("Words: ")
x = ask.split()
for i in x:
    if i[0] in vowels:
        list.append(i)
list.sort()
print(" ".join(list))