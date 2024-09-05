#This program prompts the user for sales amounts
#and writes those amounts to the sales.txt file.
#Get the number of days.
num_day = int(input("For how many days do you have sales?"))
#Open new file named sales.txt using with statement
with open("sales.txt", "w") as sales_file:
    for count in range(1, num_day + 1):
        sales = float(input(f"Enter the sales for day #{count}: "))
        sales_file.write(str(sales) + "\n")

print("Data written to sales.txt")