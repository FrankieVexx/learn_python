temp = int(input("What is the temparature outside:? "))
if temp >= 0 and temp <= 30:
    print("The temparature is good today")
    print("Go outside and have fun")
elif temp < 0 or temp > 30:
    print("The temparature is bad today")
    print("Stay inside")