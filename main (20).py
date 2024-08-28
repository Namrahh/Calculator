# Calculator

# Add 
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

# divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

num1 = int(input("Enter your first number: "))
for symbol in operations:
  print(symbol)

should_continue = True
while should_continue:

  operation_symbol = input("Pick an operation from the line above: ")
  num2 = int(input("Enter your next number: "))

  calculation_ftn = operations[operation_symbol]

  answer = calculation_ftn(num1, num2)
  print(f"{num1} {operation_symbol} {num2} = {answer}")

  if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") == "y":
    num1 = answer
  else:
    should_continue = False


# operation_symbol = input("Please pick another operation: ")
# num3 = int(input("Enter your third number: "))
# calculation_ftn = operations[operation_symbol]
# second_answer = calculation_ftn(first_answer, num3)
# print(f" {first_answer} {operation_symbol} {num3} = {second_answer}")

  
  
  

