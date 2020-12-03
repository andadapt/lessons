total = 0
another = ""

while another != "n":
    x = int(input("enter a number to add"))
    total = total + x
    another = input("Do you want to enter another number? y or n")

print("your total is ", total)
    