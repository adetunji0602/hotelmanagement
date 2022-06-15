#Multiplication table of number between 1 to 10 

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end=" ")
#     print("\t\t")

#Calculate the multiplication and sum of two numbers
def mult(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

result = mult(20, 30)
print("The result 1 is", result)

result = mult(40,30)
print("The result 2 is", result)