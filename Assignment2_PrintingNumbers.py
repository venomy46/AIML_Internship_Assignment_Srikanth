#1. Print whether a number is odd or even
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

#2. Print numbers from 10 to 1
for i in range(10, 0, -1):
    print(i)

#3. Sum until the user stops (enter 0 to stop)
total = 0

while True:
    num = int(input("Enter a number (0 to stop): "))
    
    if num == 0:
        break
    
    total = total + num

print("Total sum is:", total)