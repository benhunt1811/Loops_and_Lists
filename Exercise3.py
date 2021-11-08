Password = "Banana"
tries = 3
while True:
  guess = input("Guess: ")
  if guess == Password:
    print("Hooray")
    break
  else:
    tries -= 1
  if tries == 0:
    print("You Lost")
    break
