#Lesson00, Andra Rice

print("Enter an integer betweeen 1 and 100:")

x=input() #read input from user

x=int(x) #typecast x so we can make sure it's in the bounds!

if x<1 or x>100:
    print("The input entered does not meet the conditions.")
    
    while x<1 or x>100: #continue to ask for new input until a reasonable int is entered
        print("Enter an integer betweeen 1 and 100:")
        x=input()
        x=int(x) #typecast x

range=range(1,x+1)
i=1

#print a number triangle 
for i in range:
    j=1
    while j<=i:
        print(i, end='')
        print(" ", end='')
        j=j+1
    print("")



