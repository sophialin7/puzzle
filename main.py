# Welcome to the Puzzle Escape Room!
# Solve these simple puzzles to complete the challenge!
# First, we want to figure out why the program is not executing, and fix bugs in our code!

print('Welcome to the Puzzle Escape Room!')
admission = inpot('Ready to start? Enter y for yes, n for no')

if admission == 'y':
  print('Alright, time to get started! Pretend that you are about to embark on a journey around the world. \nAs you stroll down a cobblestone path lined with quirky antique shops filled with almanacs, you encounter a brick wall with lines drawn in white ink coming together to represent a shape like a lion! Curious, you draw closer and examine the art, and your foot accidentally stumbles upon a spring at the bottom of the wall. \nThe wall shivers, and a hologram appears with a puzzle you must solve to enter')
  
  ''' 
  digit = 9+8*6/(2*4)
  food = 'spongecakes'
  
  We have not covered this concept yet, but with strings there are built-in functions you can use to make the letters uppercase .upper() and lowercase .lower()
  
  food[0:6].upper()
  secret_password = digits + password
  '''
  answer = input('Please enter the secret_password: ')
  
  if answer == secret_password:
    print("The wall starts to crumble and reveal a path to the castle decorated with plants and covered with moss")
  else:
    answer = input('Please enter the secret_password: ')
    
elif admission = 'n':
  admission = input('There's only one correct answer Enter y for yes, n for no')
  
