rows = int(input("Enter the size of the pattern: "))
temp = rows

while rows > 0:
  for i in range(temp):
    print("*" , end="")
  print()
  rows -=1