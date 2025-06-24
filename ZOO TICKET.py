print("Welcome to the zoo trip!")

age = int(input("To enter the zoo, we need your age: "))
height = int(input("Enter your height in cm: "))
bill = 0

if age >= 18 and height > 110:
    print("You can go inside!")

    bill_age = int(input("For billing, please enter your age again: "))

    if 18 <= bill_age <=20:
        bill = 20
        print("You need to pay $20.")
    elif 21 <= bill_age <= 30:
        bill = 25
        print("You need to pay $25.")
    elif bill_age >=30:
        bill = 40
        print("You need to pay $40. And please don't touch the animals — you uncles are crazy!")

    photo_choice = input("Do you want a photo? Type 'yes' or 'no': ").lower()
    if photo_choice == "yes":
        bill += 3
        print("You need to pay an extra $3 for the picture. Don't worry, you look great in it!")

    print(f"Total bill: ${bill}")
    if photo_choice =="no":
        print(f"your bill is ${bill}")
elif age >= 18 and height <= 110:
    print("Your age is okay, but your height doesn't meet the requirement. Eat some protein, man!")
else:
    print("You're too young. Grow up, man!")
