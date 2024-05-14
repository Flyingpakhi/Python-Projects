print("welcome to my computer quiz!")
# check if user want to play the quiz or not
playing=input("Do you want to play? " )
# if player answers other than yes,quit the game
# it can take any typing of yes
# Return a copy of the string converted to lowercase.
if playing.lower()!='yes':
    quit()
print("okay! Let's start playing :)")
count=0
# question no 1
answer=input("what does cpu stands for? ")
if answer.lower()=="central processing unit":
    print("correct")
    count=count+1
else:
    print("incorrect")
# question no 2
answer=input("what does RAM stands for? ")
if answer.lower()=="random access memory":
    print("correct")
    count=count+1
else:
    print("incorrect")
# question no 3
answer=input("what does ROM stands for ? ")
if answer.lower()=="read only memory":
    print("correct")
    count=count+1
else:
    print("incorrect")
# question no 4
answer=input("what does gpu stands for? ")
if answer.lower()=="graphics processing unit":
    print("correct")
    count=count+1
else:
    print("incorrect")

# count the score
# we need to do str(count) as we can't concat int with string so convert int to str first.
print("your score is: "+str(count)+" out of 4")
# show the percentage
print("your score is: "+str((count/4)*100)+" pecent")
print("meet you again!!")
