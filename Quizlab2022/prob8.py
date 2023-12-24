#Problem8 Final labquiz2022

def BinaryConversion(n):
    if n > 1:
        BinaryConversion(n//2)
    remainder = n % 2
    print(remainder, end = "")
while True:
    num = input("Enter a decimal number ('done' for exit): ")
    if num.lower() == "done":
        break
    if num.isnumeric():
        num = int(num)
        print("Binary number of %d is "%(num), end = "")
        BinaryConversion(num)
        print(".")
    else:
        print("Wrong Input. Please enter a decimal number again.")



# def BinaryConversion(num):
#     """This function converts decimal number
#     to binary and prints it"""
#     if num > 1:
#         BinaryConversion(num // 2)
#     print(num % 2, end='')


# # decimal number
# number = int(input("Enter any decimal number: "))

# BinaryConversion(number)