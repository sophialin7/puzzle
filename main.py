# Welcome to the Puzzle Escape Room!
# Solve this puzzle to complete the challenge and escape!
# First, we want to figure out why the program is not executing, and fix bugs in our code!

print('Welcome to the Puzzle Escape Room!')
admission = inpot('\nReady to start? Enter y for yes, n for no: ')

# Here we have an if statement, where we evaluate if the variable admission is set to 'y'. If that is correct, then the print statement will execute!
if admission == 'y':
  print('\nAlright, time to get started! \nAs you stroll down a cobblestone path lined with quirky antique shops filled with almanacs, you encounter a brick wall with lines drawn in white ink coming together to represent a shape like a lion! Curious, you draw closer and examine the art, and your foot accidentally stumbles upon a spring at the bottom of the wall. \nThe wall shivers, and a hologram appears with a puzzle you must solve to enter')
  
  ''' 
  digit = 9+8*6/(2*4)
  food = 'spongecakes'
  
  We have not covered this concept yet, but with strings there are built-in functions you can use to make the letters uppercase by using .upper() or lowercase by using .lower()
  There is also a concept called indexing, where we refer to each letter as a number, and we can modify or retrieve a certain letter by using the number it is associated with.
  We enclose the numbers with square brackets [], and note that indexing starts at 0. If you are starting at 0, then you are retrieving the first value in a data type (in this case is a string)
  
  food = food[0:6].upper() + food[6:]
  
  # Here is the secret password! Combine the variables 'digit' and 'food' declared in line 13 to unpack the secret password!
  secret_password = digits + password
  '''
  answer = input('\nPlease enter the secret_password: ')
  
  if answer == secret_password:
    print("The wall starts to crumble and reveal a path to the castle decorated with plants and covered with moss")
  else:
    answer = input('Please enter the secret_password: ')

# Here we have an elif statement; if the if statement above was not true, then the computer checks if this elif statement is true. If it is true, then the computer will execute the code block!
elif admission = 'n':
  admission = input('There's only one correct answer. Enter y for yes, n for no: ')
  
