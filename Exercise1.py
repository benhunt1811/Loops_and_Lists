list1 = ["Xavier", "Ben", "Louis", "Xander", "Alasdair"]
list2 = []
list3 = []
x = 0
length = len(list1)
while True:
  first_char = list1[x][0]
  name = list1[x]
  if first_char == "X":
    list2.append(name)
  else:
    list3.append(name)
  x = x + 1
  if x == length:
    break

print("done")
print(list2 + list3)
