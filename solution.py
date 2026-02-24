print("Library Fine")

days = int(input("Enter late days: "))

if days > 5:
    fine = days * 10
else:
    fine = 0

print("Fine:", fine)

for i in range(3):
    print("Paid")

print("Exit")
