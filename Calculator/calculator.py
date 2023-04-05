def add(n1, n2):
  return n1+n2

def subtract(n1, n2):
  return n1-n2

def multiply(n1, n2):
  return n1*n2

def divide(n1, n2):
  return n1/n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}

repeat = True

num1 = float(input("What's the first number? : "))
for key in operations:
  print(key)

while(repeat):
  operation = input("Pick an operation from above: ")
  num2 = float(input("Input the next number : "))
  calop = operations[operation]
  answer = calop(num1,num2)
  print(f"{num1} {operation} {num2} = {answer}")

  choice = input("Continue using the answer? 'y' or 'n': ")
  
  if(choice == 'y'):
    num1 = answer
  else:
    repeat = False