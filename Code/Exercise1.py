num_peo = int(input("How many records do you want to create? "))
with open("people.txt", "a") as rec_file:
    for count in range(1, num_peo + 1):
        print("Enter data #", count, sep="")
        name = input("Name: ")
        id_num = input("ID number: ")
        dept = input("Department: ")

        rec_file.write("Name:" + name + "\n")
        rec_file.write("ID:" + id_num + "\n")
        rec_file.write("Department:" + dept + "\n")
        print()

print("The records written to people.txt")