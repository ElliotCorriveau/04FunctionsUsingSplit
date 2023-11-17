expression = input("Please enter your expression.")
num1, sign, num2 = expression.split(" ")
num1 = int(num1)
num2 = int(num2)
if sign == ("+"):
  print(num1 + num2)
if sign == ("*"):
  print(num1 * num2)
if sign == ("-"):
  print(num1 - num2)
if sign == ("/"):
  print(num1 / num2)
