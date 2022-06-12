import random

input ( "Welcome!, Press enter to start")


while True:
  print()
  Player_choice = input( "Rock,Paper or Scissors ?: ").lower()
  while Player_choice != "Rock" and Player_choice != "Paper" and Player_choice != "Scissors":
   Player_choice = input ("Invalid, please try again: ").lower()
   
   random_n = random.randint (0,2)
   if random_n == 0:
    cpu_choice = "rock"
   elif random_n == 1:
    cpu_choice = "paper"
   elif random_n == 2:
    cpu_choice = "scissors"


   print( )
   print ("Your choice :",Player_choice)
   print  ("CPU  choice :",cpu_choice) 
   print ( )

   if Player_choice == "rock":
      if cpu_choice == "rock":
         print ("It's a tie!")
      elif cpu_choice == "paper":
         print ("You lost!") 
      elif  cpu_choice == "scissors":
         print ("You win!") 
   elif Player_choice == "paper":
      if cpu_choice == "paper":
         print ("It's a tie!")
      elif cpu_choice == "scissors":
         print ("You lost!") 
      elif  cpu_choice == "rock":
         print ("You win!")
   elif Player_choice == "scissors":
      if cpu_choice == "scissors":
         print ("It's a tie!")
      elif cpu_choice == "rock":
         print ("You lost!") 
      elif  cpu_choice == "paper":
         print ("You win!")
   
   
   repeat = input("Will you like to play again?(Y/N) ").lower()
   while repeat != "n" and repeat != "n":  
      repeat = input("Input invalid, please try again: ").lower( )

   if repeat == "n":
    break




 