num = input("Enter a valid numerical score between 0 and 100: ")
while not num.isdigit():
    num = input("Enter a valid numerical number between 0 and 100: ")
num = int(num)
while num < 0 or num > 100:
    num = int(input("Enter a valid numerical number between 0 and 100: "))

if 90<=num<=100:
    grade = "A"
elif 80<=num<=89:
    grade = "B"
elif 70<=num<=79:
    grade = "C"
elif 60<=num<=69:
    grade = "D"
else:
    grade = "F"

print(f"your Grade is: {grade}")
