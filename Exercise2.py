list1 = ["xavier", "ben", "louis", "xander", "alasdair", "hannah"]
x = 0
length = len(list1)
while True:
  first_char = list1[x][0]
  name = list1[x]
  name_length = len(name)
  last_char = list1[x][name_length - 1]
  if first_char == last_char and name_length >= 2:
    print(name)
  x = x + 1 
  if x == length:
    break
