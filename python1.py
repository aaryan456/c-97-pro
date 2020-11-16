import random

number = random.randint(1, 21)

guessno = int(input("Enter from 1 to 99: "))

while number != "guess":

  print

  if guessno < number:

    print ("guess is low")

    guessno = int(input("TRY AGAIN :( "))

  elif guessno > number:

    print ("guess is high")

    guessno = int(input("TRY AGAIN :( "))

  else:

    print ("you guessed it :p")