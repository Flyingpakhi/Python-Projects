# random module is in built module present in python
import random

# let's user give the top range
top_of_range=input("type a top range: ")
# check if the top of range is digit or not
if top_of_range.isdigit():
    # if digit,then greater than 0 or not
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print('Please type a number greater than 0 next time')
        quit()
else:
    print('Please enter a number next time')
    quit()
# both are used to generate random integer
# random.randrange(start,stop)->start is included but stop is not
# random.randint(start,stop)->start and stop both are included
r=random.randint(0,top_of_range)
# count the number of guess
guess=0
print("enter a number between 0 to ",top_of_range)
while True:
    guess_number=input("enter a number: ")
    if guess_number.isdigit():
        guess_number=int(guess_number)
    else:
        print('Please enter a number next time')
        continue
    # if guess number is the right number
    if(guess_number==r):
        guess+=1
        print("your guess is correct :)")
        break
    if guess_number<0:
        print("enter a number between 0 to ",top_of_range)
        guess+=1
    elif guess_number>r:
        print("your guess is more than the actual number!! Lower the number")
        guess+=1
    else:
        print("your guess is lesser than the actual number!! Upper the number")
        guess+=1
# count the number of guess
print("you guess the right number in "+str(guess)+" time")
print("play again!!")




