dict = {}

# list.append((3+2, 4))
# list.append((2, 4))

dict[(3, 4)] = "m"
dict[(2,5)] = "t"

print(dict)

if (3,4) in dict:
    print("trovato" + dict[(3,4)])