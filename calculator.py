import os
import time
import calc_art
def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}

def do_more(previous_answer):
  for sign in operations:
    print(sign)
  symbol = input("Pick an operation--> ")
  num3 = float(input("What's the next number? -> "))
  function = operations[symbol]
  answer = function(int(previous_answer) , num3)
  print(f"{previous_answer} {symbol} {num3} = {answer}")
  choice = input(f"Do you want to continue this calculation with {answer}?'y' or 'n': ")
  if(choice == "y"):
    do_more(answer)


is_continue = True
while(is_continue):
  print(calc_art.logo)
  num1 = float(input("What's the first  number? -> "))
  
  for sign in operations:
    print(sign)
  
  operation_symbol = input("Pick an operation from the line above? --> ")
  num2 = float(input("What's the second number? -> "))
  function = operations[operation_symbol]
  answer = function(num1, num2)
  
  print(f"{num1} {operation_symbol} {num2} = {answer}")
  is_continue = input(f"Do you want to continue this calculation with {answer}?'y' or 'n': ")
  if(is_continue == "y"):
    do_more(answer)
    time.sleep(0.1)
    os.system('clear')
  else:
    is_continue = False