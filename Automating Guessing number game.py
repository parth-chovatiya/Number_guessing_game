import random
def computerGuess(lowval, highval, randnum , counts =0):
    if highval >=lowval:
        guess = lowval + (highval - lowval) // 2
        #If guess is in the middle ,it is found !
        if guess == randnum:
            print(guess)
            return counts
        # if "guess" is greater than Number,
        # it must be found in the lower half of the set of number
        # between the lower value and the guess
        elif guess > randnum:
            print(guess)
            counts =counts +1
            return computerGuess(lowval ,guess-1, randnum ,counts)
        #The number must be in upper set of number
        #Between the guess and the upper value
        else :
            print(guess)
            counts = counts +1
            return computerGuess(guess + 1, highval ,randnum,counts)
            
    else:
        #Number not found
        return -1
#end of function
#Gernerate a random number in 1 to 100
randnum=random.randint(1,100)

count=0
guess=101

print("Let's start the Game ")

while(guess != randnum):
    #Let's take the sample input from the user 
    guess=int (input("Enter the number between 1 to 100 : "))
   
    if (guess > randnum):
        print("Higher")
        #it means the guess no is higher than the user input
    elif(guess < randnum):
        print("Lower")
        #it means the guess no is lower than the user input

    else:
        print("You got it !!")
        #it means the guess no is equal to the user input
    count=count+1   
    #it gives us the no of steps taken 

print("Let's give the same task to the computer ")
#lets call the function
counts=computerGuess(0,100,randnum)
#it return us only count 
print ("computer took " + str(counts) + " steps !")

computer_step=counts
user_steps=count

print("You took "+str(count)+" steps to guess the Number")
# comparision between user and computer 
if user_steps < computer_step:
    print("You won the Game")
    print("Congrat..")
elif (user_steps == computer_step):
    print("Hahahahaha!!!!!!! \n You and computer took same steps to complete the Game \n Play again!!")
else:
    print("Computer won the Game !")
