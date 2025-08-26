from random import randint

print('Enter the lowest number')
low = int(input())
high = int(input('Enter the highest number:  '))
tries = 5

while high <= low:
  print(f"Please enter the higher number than {low}")
  high = int(input('Enter the highest number:  '))
correct = randint(low, high)
print(f'Guess a number between {low}, {high}.')
while tries > 0:
  guess = int(input())
  if guess < correct:
    print('Guess higher!')
  elif guess > correct:
    print('Guess lower!')
  else:
    print('You win')
  tries -=1
  print(f'Tries left: {tries}')
  if tries == 0:
    print(f'You lost! The correct number was {correct}')
    break
