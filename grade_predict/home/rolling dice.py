'''import random
hidden = random.randrange(1,21)
print("The hidden values is",hidden)
user_input=input("Please enter your guess: ")
print(user_input)
guess=int(user_input)
if guess == hidden:
    print("Hit!")
elif guess < hidden:
    print("Your guess is too low")
else:
    print("Your guess is too high")'''
from rembg import remove
from PIL import Image
input_path ='C:\Users\uniqu\Pictures\gfgimage.png'
output_path ='C:\Users\uniqu\Pictures\gfgimage.png'
inpput=Image.open(input_path)
output = remove(input)
output.save(output_path)