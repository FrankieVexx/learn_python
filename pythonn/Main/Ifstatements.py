# If statement is a block of code that executes only if a condition is true
age = int(input("How old are you?: "))

if age >= 18 and age < 69:
    print("You are an adult")
elif age < 50:
    print("You are still young")
elif age >= 70:
    print("You are old")
else:
    print("You are a child")