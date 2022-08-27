import random
name = input("Enter the name:")
print("Enter the range:")
st, end = map(int , input().split('-'))

x = random.randint(st, end)

count = 0
score = 50

while (score!=0):
    y = int(input("Guess the number:"))
    if x == y:
        print(f"You guessed the correct no. in {count} guesses.")
        print(f"you got {score} points.")
        break
    else:
        score = score - 5
        count = count+1
        print ("hint")
        if x > y:
            print("Try greater than that number.")
        else:
            print("Try smaller number than that.")
        if(x%2==0):
            print("Try even number")
        else:
            print("Try odd number")
