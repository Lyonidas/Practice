# Preston Hudson 11/20/19 Challenge 3 Written in Python

#1. Print three seperate strings.

print("This is the tale of Preston Hudson.")
print("A software engineer learning Python.")
print("Will he finish? The world may never know.")

#2. Print if a variable is less then or greater then 10.

prestons_age = 24

if prestons_age < 10:
    print("Preston is still a child.")
elif prestons_age >= 10:
    print("Preston is a old man. XD")

#3. print if a variable is less then or equal to 10, greater then 10 or greater then 25.

if prestons_age <= 10:
    print("Preston is a child.")
elif prestons_age > 10 and prestons_age <= 25:
    print("Preston is a young adult/teenager.")
elif prestons_age > 25:
    print("Preston is a adult.")

#4. Create a program that divides two variables and prints the remainder.

x = 104 % 5
print(x)

#5. Create a program that divides two variables and prints the quotient.

y = 104 // 5
print(y)

#6. Write a program that has a "age" and have that age print different strings depending on age.

age = 24

if age < 3:
    print("You are a baby.")
elif age >= 3 and age <= 10:
    print("You are a child.")
elif age > 10 and age <= 12:
    print("You are a pre-teen.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
elif age >= 20 and age < 25:
    print("You are a young adult.")
elif age >= 25 and age < 65:
    print("You are a adult.")
elif age >= 65:
    print("You are a senior.")


#Complete
