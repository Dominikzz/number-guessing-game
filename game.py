import random
import datetime

computer_number = random.randint(1, 100)
user_guesses = []
start_time = datetime.datetime.now()



while(True):
  user_guess = int(input('Uzmini skaitli starp 1 un 100: '))
  user_guesses.append(user_guess)
  if user_guess == computer_number:
    print('Precīzi, tu uzminēji')
    break
  elif user_guess < computer_number:
    print('Vairāk')
  elif user_guess > computer_number:
    print('Mazāk')
  else: 
    print('Error')

print('Game Over!')

sum_of_differences = 0
for n in user_guesses:
 sum_of_differences += abs(n - computer_number)
 
 
print(f'Vidējā starpība ir {sum_of_differences/len(user_guesses)}')
print(f'Tu spēlēji {datetime.datetime.now() - start_time} sekundes
