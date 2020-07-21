#loop to repeat "for" loops and add +1

length = int(input("How long would you like the stack to be \n"))
for j in range(1, length+1):
  for i in range(1, j+1):
   print(i, end = " ")
  print()
