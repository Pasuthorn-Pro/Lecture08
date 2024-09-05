with open("sales.txt", "r") as sales_file:
    sales_file = sales_file.readlines()

total = 0

for line in sales_file:
    amount = float(line)
    print(format(amount, ".2f"))
    total += float(line.strip())

print(f"The total sales of al day is: ${total: .2f}")