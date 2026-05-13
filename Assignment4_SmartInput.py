#Assignment (12/02/2026)
#Assignment Name: Smart Input 
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

# Categorizing age
if age < 13:
    category = "a child"
elif age < 20:
    category = "a teenager"
elif age < 60:
    category = "an adult"
else:
    category = "a senior citizen"

# Personalized message
print("\nHello", name + "!")
print("You are", category, "and you enjoy", hobby + ".")
print("That's awesome! Keep enjoying your hobby!")