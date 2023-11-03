list = []
ask = input("Country: ")
list.append(ask)
while ask != "":
    ask = input("Country: ")
    if ask != "":
        list.append(ask)

print("Greece")
for i in list:
    print(i)
print("Refugee Olympic Team")
print("Japan")