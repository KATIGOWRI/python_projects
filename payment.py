


print("Welcome to the tip calculator!")

amount = float(input("Please enter the total bill: $"))
tip_choice = input("Do you want to give a tip to our service? Type YES, NO, or CUSTOM: ").lower()

tip_percent = 0

if tip_choice == "yes":
    tip_percent = int(input("Enter the tip percentage (e.g. 10, 12, 15): "))
elif tip_choice == "custom":
    tip_percent = int(input("Enter your custom tip percentage: "))
elif tip_choice == "no":
    print("No tip selected.")
else:
    print("Invalid option. Proceeding with 0% tip.")
print("Do you want to split the bill")
Options = input('if "YES" Enter yes or No or Skip').lower()
num_people=1
if Options == "yes":
    try:
        num_people=int(input('Enter how many people you want to split'))
        if num_people < 1:
            print("invalid number we are uesing it has zero")
            num_people=1
    except ValueError:
            print("To split the bill we need alteast 2people we are take it has zero sorry")

payment_method = input("Do you want to PAY THE BILL BY CARD OR CASH? ").lower()

tip_amount = (tip_percent / 100) * amount
total_amount = amount + tip_amount
split_bill = total_amount/num_people

print("\n------ BILL SUMMARY ------")
print(f"Tip amount: ${tip_amount:.2f}")
print(f"split amount:${num_people} the amount spilted")
print(f"the total ammout need to pay by each person is {split_bill:}")
print(f"Total amount is : ${total_amount:.2f}")
print(f"Payment method: {payment_method.upper()}")
print("Thank you!")



