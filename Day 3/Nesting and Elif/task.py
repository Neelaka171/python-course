print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("what is your age:"))
    if  50> age >18 :
        print("50 rupees ticket")
    elif  age > 50:
        print("100 rupees ticket")
    else:
        print("free")
else:
    print("Sorry you have to grow taller before you can ride.")
