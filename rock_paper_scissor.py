import random
user_score=0
comp_score=0
# make a list of rock,paper and scissor
options=["rock","paper","scissors"]

while True:
    user_input=input("enter rock,paper,scissors or Q to quit ").lower()
    if user_input=='q':
        break
    if user_input not in options:
        continue
    # rock->0,paper->1,scissor->2
    comp_guess=random.randint(0,2)
    comp_pick=options[comp_guess]
    print("computer input: ",comp_pick)
    if (user_input=="rock" and comp_pick=="scissors") or (user_input=="paper" and     comp_pick=="rock") or (user_input=="scissors" and comp_pick=="paper"):
        print("user wins here :)")
        user_score+=1
    elif (comp_pick=="rock" and user_input=="scissors") or (comp_pick=="paper" and     user_input=="rock") or (comp_pick=="scissors" and user_input=="paper"):
        print("comp wins here :)")
        comp_score+=1
    else:
        print("match is draw,noone wins!!")

print("overall score: ")
print("user wins: ",str(user_score)+" times")
print("computer wins: ",str(comp_score)+" times")
